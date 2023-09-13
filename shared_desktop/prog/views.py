from django.shortcuts import render

def prog(request):
    """Программирование ДК."""
    template = 'prog/prog.html'
    prog = 'programs'
    context = {
        'prog': prog,
    }
    return render(request, template, context)
