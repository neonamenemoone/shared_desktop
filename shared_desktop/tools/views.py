import socket
from django.http import JsonResponse
from django.forms import modelformset_factory
from django.shortcuts import render
from pysnmp.hlapi import *
from tools.forms import ControllerForm
from tools.models import Central

def is_valid_ip(ip_address):
    try:
        socket.inet_pton(socket.AF_INET, ip_address)
        return True
    except socket.error:
        return False

def tools(request):
    """Инструменты."""
    template = "tools/tools.html"
    tools = "tools"
    context = {
        "tools": tools,
    }
    return render(request, template, context)

def calculate_cycle(request):
    """Таблица направлений."""
    template = "tools/calculate_cycle.html"
    return render(request, template)

def phase_control(request):
    """Управление фазой контроллера."""
    template = "tools/phase_control.html"
    community_string = "private"
    error_message = ""
    new_value = 0
    ip_address = ""
    command_value = ""
    status_value = ""

    if request.method == 'POST':
        # Обработка POST-запроса для обновления фазы
        ip_address = request.POST.get('ip_address')
        if not is_valid_ip(ip_address):
            error_message = "Некорректный IP-адрес"
        else:
            new_value = int(request.POST.get('phase_value'))
            oid = ObjectIdentity("1.3.6.1.4.1.1618.3.7.2.11.1.0")

            error_indication, error_status, error_index, var_binds = next(
                setCmd(SnmpEngine(),
                       CommunityData(community_string, mpModel=0),
                       UdpTransportTarget((ip_address, 161)),
                       ContextData(),
                       ObjectType(oid, Unsigned32(new_value))))

            if error_indication:
                error_message = f"Ошибка: {error_indication}"
            else:
                error_message = None

    elif request.method == 'GET':
        # Обработка GET-запроса для получения текущего статуса
        if 'get_status' in request.GET:
            ip_address = request.GET.get('ip_address')
            if not is_valid_ip(ip_address):
                error_message = "Некорректный IP-адрес"
            else:
                new_value = int(request.GET.get('phase_value', 1))
                command_oid = ObjectIdentity("1.3.6.1.4.1.1618.3.7.2.11.1.0")
                status_oid = ObjectIdentity("1.3.6.1.4.1.1618.3.7.2.11.2.0")

                error_indication, error_status, error_index, var_binds = next(
                    getCmd(SnmpEngine(),
                           CommunityData(community_string),
                           UdpTransportTarget((ip_address, 161)),
                           ContextData(),
                           ObjectType(command_oid),
                           ObjectType(status_oid))
                )

                if error_indication:
                    error_message = f"Ошибка: {error_indication}"
                else:
                    command_value = var_binds[0][1].prettyPrint()
                    status_value = var_binds[1][1].prettyPrint()

                    if int(command_value) > 0:
                        command_value = str(int(command_value) - 1)

                    if int(status_value) > 0:
                        status_value = str(int(status_value) - 1)

    # Создайте список значений для фазы
    phase_values = [
        (0, 'LOCAL'),
        (2, '1 фаза'),
        (3, '2 фаза'),
        (4, '3 фаза'),
        (5, '4 фаза'),
        (6, '5 фаза'),
        (7, '6 фаза'),
        (8, '7 фаза'),
        (1, '0 фаза'),
    ]

    # Выберите значение по умолчанию
    selected_phase = None
    for value, label in phase_values:
        if new_value == value:
            selected_phase = value
            break

    if request.is_ajax():
        return JsonResponse({'status': status_value})

    return render(
        request, template, {
            'ip_address': ip_address,
            'error_message': error_message,
            'new_value': new_value,
            'command': command_value,
            'status': status_value,
            'phase_values': phase_values,
            'selected_phase': selected_phase
        }
    )

def technical_coordination(request):
    """Техническая координация."""
    template = "tools/technical_coordination.html"
    community_string = "private"
    error_message = ""
    ControllerFormSet = modelformset_factory(Central, form=ControllerForm, extra=8) 

    if request.method == 'POST':
        formset = ControllerFormSet(request.POST, queryset=Central.objects.none()) 

        for form in formset:
            if form.has_changed():
                ip_address = form['ip_address'].value()
                phase_value = int(form['phase_value'].value())
                button_name = next(
                    (k for k, v in request.POST.items() if k.startswith('apply_button_')),
                    None
                )
                if button_name:
                    form_number = int(button_name.replace('apply_button_', ''))
                    if not is_valid_ip(ip_address):
                        error_message = "Invalid IP Address"
                    else:
                        oid = ObjectIdentity("1.3.6.1.4.1.1618.3.7.2.11.1.0")

                        error_indication, error_status, error_index, var_binds = next(
                            setCmd(SnmpEngine(),
                                CommunityData(community_string, mpModel=0),
                                UdpTransportTarget((ip_address, 161)),
                                ContextData(),
                                ObjectType(oid, Unsigned32(phase_value))
                            )
                        )

                        if error_indication:
                            error_message = f"Ошибка: {error_indication}"
                        else:
                            error_message = None

        return render(request, template, {'formset': formset})
    else:
        formset = ControllerFormSet(queryset=Central.objects.none())

    return render(request, template, {'formset': formset})
