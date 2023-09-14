from django.contrib.auth.decorators import login_required
from django.http import HttpResponse
from django.shortcuts import render

from .models import Rule


def index(request):
    """Главная страница."""
    template = "board/index.html"
    # text = 'Правила'
    rules = Rule.objects.order_by("-pub_date")[:30]
    context = {
        "rules": rules,
    }
    return render(request, template, context)


@login_required
def full(request):
    """Главная страница с метаданными."""
    template = "board/full.html"
    # text = 'Правила'
    rules = Rule.objects.order_by("-pub_date")[:30]
    context = {
        "rules": rules,
    }
    return render(request, template, context)


def rules_list(request):
    return HttpResponse("Правила")


def rules_detail(request, pk):
    return HttpResponse(f"Правило {pk}")
