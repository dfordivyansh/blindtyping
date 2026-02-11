from django.db import models
from django.contrib.auth.models import User

class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    full_name = models.CharField(max_length=200)
    contact_number = models.CharField(max_length=20)
    branch = models.CharField(max_length=100)
    year = models.CharField(max_length=20)

    def __str__(self):
        return self.user.username
