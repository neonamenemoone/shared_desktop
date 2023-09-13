from django.shortcuts import render

def prog(request):
    """Программирование ДК."""
    template = 'prog/index.html'
    prog = 'programs'
    context = {
        'prog': prog,
    }
    return render(request, template, context)
