from django.http import HttpResponse


def index(request):
    return HttpResponse('У меня получилось обновить проект и автоматически его запустить на сервере!!!')


def second_page(request):
    return HttpResponse('А это вторая страница!')
