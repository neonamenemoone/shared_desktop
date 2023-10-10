from django.shortcuts import render
from pysnmp.hlapi import *

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

def technical_coordination(request):
    """Управление фазой контроллера."""
    template = "tools/technical_coordination.html"
    community_string = "private"
    error_message = ""
    new_value = 1
    ip_address = ""
    command_value = ""
    status_value = ""

    if request.method == 'POST':
        # Обработка POST-запроса для обновления фазы
        ip_address = request.POST.get('ip_address')
        new_value = int(request.POST.get('phase_value'))

        oid = ObjectIdentity("1.3.6.1.4.1.1618.3.7.2.11.1.0")

        error_indication, error_status, error_index, var_binds = next(
            setCmd(SnmpEngine(),
                   CommunityData(community_string, mpModel=1),
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
        (0, 'Выкл'),
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
