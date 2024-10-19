# myapp/forms.py

from django import forms
from .models import Client, SystemInfo

class ClientForm(forms.ModelForm):
    class Meta:
        model = Client
        fields = ['first_name', 'last_name']

class SystemInfoForm(forms.ModelForm):
    class Meta:
        model = SystemInfo
        fields = ['os', 'os_version', 'cpu_count', 'cpu_freq', 
                  'cpu_usage', 'total_memory', 'used_memory', 
                  'memory_percent', 'total_disk', 'used_disk', 
                  'disk_percent']  # Use actual fields from SystemInfo model