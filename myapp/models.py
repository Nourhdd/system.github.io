# myapp/models.py

from django.db import models

class Client(models.Model):
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)

    def __str__(self):
        return f"{self.first_name} {self.last_name}"
class SystemInfo(models.Model):
    client = models.ForeignKey(Client, on_delete=models.CASCADE, null=True)  # Make nullable for now
    os = models.CharField(max_length=100)
    os_version = models.CharField(max_length=100)
    cpu_count = models.IntegerField()
    cpu_freq = models.FloatField()
    cpu_usage = models.FloatField()
    total_memory = models.BigIntegerField()
    used_memory = models.BigIntegerField()
    memory_percent = models.FloatField()
    total_disk = models.BigIntegerField()
    used_disk = models.BigIntegerField()
    disk_percent = models.FloatField()

    def __str__(self):
        return f"System Info for {self.client} - {self.os}"  # Update this to include client
