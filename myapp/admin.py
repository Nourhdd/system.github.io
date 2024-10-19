from django.contrib import admin
from .models import Client, SystemInfo

admin.site.register(Client)
admin.site.register(SystemInfo)