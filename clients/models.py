from django.db import models

class Client(models.Model):
    clientId = models.AutoField(primary_key=True)
    fullName = models.CharField(max_length=100)
    phone = models.CharField(max_length=20)
    email = models.EmailField(unique=True)
    cniNumber = models.CharField(max_length=20, unique=True)
    state = models.SlugField(choices=[('active', 'Active'), ('inactive', 'Inactive')], default='active')
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"{self.fullName}"
