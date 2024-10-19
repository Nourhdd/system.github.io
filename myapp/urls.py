from django.urls import path
from . import views

urlpatterns = [
    
     path('sys/', views.system_info_view, name='system_info'),  # Ajoutez un chemin vers votre vue
]