
from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('recipes.urls')),
    path('recipes/', include('recipes.urls')), #dominio com recipes
]
