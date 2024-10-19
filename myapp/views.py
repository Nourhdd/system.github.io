from django.http import HttpResponse
from django.shortcuts import render, redirect
import platform
import psutil

from .forms import ClientForm, SystemInfoForm
from .models import Client, SystemInfo

def system_info_view(request):
    if request.method == 'POST':
        # Create and save client instance
        first_name = request.POST.get('first_name')
        last_name = request.POST.get('last_name')
        client = Client.objects.create(first_name=first_name, last_name=last_name)

        # Collect system information using psutil
        system_info = {
            'client': client,  # Link the system info to the newly created client
            'os': platform.system(),  # Get the OS name (e.g., 'Windows', 'Linux')
            'os_version': platform.version(),  # Get the OS version
            'cpu_count': psutil.cpu_count(),
            'cpu_freq': psutil.cpu_freq().current,
            'cpu_usage': psutil.cpu_percent(),
            'total_memory': psutil.virtual_memory().total,
            'used_memory': psutil.virtual_memory().used,
            'memory_percent': psutil.virtual_memory().percent,
            'total_disk': psutil.disk_usage('/').total,
            'used_disk': psutil.disk_usage('/').used,
            'disk_percent': psutil.disk_usage('/').percent,
        }

        # Save system information to the database
        SystemInfo.objects.create(**system_info)

        return HttpResponse("System information submitted successfully.")

    return render(request, 'system_info.html')
def add_system_info(request):
    if request.method == 'POST':
        client_form = ClientForm(request.POST)
        system_info_form = SystemInfoForm(request.POST)
        
        if client_form.is_valid() and system_info_form.is_valid():
            client = client_form.save()  # Save client info first
            system_info = system_info_form.save(commit=False)  # Don't save yet
            system_info.client = client  # Assign the client to the system info
            system_info.save()  # Now save the system info

            return redirect('some_view_name')  # Redirect to a success page or another view

    else:
        client_form = ClientForm()
        system_info_form = SystemInfoForm()

    return render(request, 'system_info.html', {
        'client_form': client_form,
        'system_info_form': system_info_form,
    })