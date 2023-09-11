from django.http import HttpResponse
from django.shortcuts import render


def index(request):
    template = 'board/index.html'
    text = 'Правила'
    context = {
        'text': text,
    }
    return render(request, template, context) 

def rules_list(request):
    return HttpResponse('Правила')


def rules_detail(request, pk):
    return HttpResponse(f'Правило {pk}') 