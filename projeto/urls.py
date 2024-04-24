
from django.contrib import admin
from django.urls import path
from django.http import HttpResponse

def my_view(request):
    return HttpResponse('UMA LINDA STRING')

def sobre(request):
    return HttpResponse('sobre')

def contato(request):
    return HttpResponse('contato')

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', my_view),
    path('sobre/', sobre), #/sobre/
    path('contato/', contato), #/contato/
]
