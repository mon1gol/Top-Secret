from django.shortcuts import render
from django.http import HttpResponse


# принимает запрос с данными о пользователе, куки,
# возвращает ответ в виде страницы
def index(request):
    context = {
        'title': 'Home',
        'content': 'Главная страница - HOME',
        'list': ['first', 'second'],
        'dict': {'first': 1},
        'bool': True,
    }

    return render(request, 'main/index.html', context)


def about(request):
    return HttpResponse('About page') 