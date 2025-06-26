from django.http import HttpResponse
from django.shortcuts import render


def home(request):
    return render(request, 'recipes/home.html', context={
        'name': 'Heder Lopes'
    }
)


def contato(request):
    return HttpResponse("<h1 style='color: yellow'><i>Contato</i></h1>")


def sobre(request):
    return HttpResponse("<h1 style='color: green'><i><a>Sobre</a></i></h1>")
