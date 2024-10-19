from django.contrib import admin
from django.urls import path, include  # Assure-toi que 'include' est importé

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('myapp.urls')),  # Utilisation de 'include' pour inclure les urls de l'application
]