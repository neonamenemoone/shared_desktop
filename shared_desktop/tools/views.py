from django.shortcuts import render


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