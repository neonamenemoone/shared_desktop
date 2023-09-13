from django.shortcuts import render

def prog(request):
    """Инструменты."""
    template = 'tools/tools.html'
    tools = 'tools'
    context = {
        'tools': tools,
    }
    return render(request, template, context)
