from django.shortcuts import render


def prog(request):
    """Программирование ДК."""
    template = "prog/prog.html"
    prog = "programs"
    context = {
        "prog": prog,
    }
    return render(request, template, context)

def equipment_layout(request):
    """Схема расположения оборудования."""
    template = "prog/equipment_layout.html"
    return render(request, template)
