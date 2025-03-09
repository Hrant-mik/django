from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.


def index(request):
    return render (request, 'main/to_do_list.html')

def set_cookie(request):
    response = HttpResponse("Cookie установлена!")
    response.set_cookie('my_cookie', 'Hello, Django!', max_age=3600)  # 1 час (3600 секунд)
    return response

def get_cookie(request):
    my_cookie = request.COOKIES.get('my_cookie', 'Нет Cookie')
    return HttpResponse(f'Значение Cookie: {my_cookie}')