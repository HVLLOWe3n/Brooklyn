from django.db import models
from django.contrib.auth.models import User


class Client(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name='client')
    avatar = models.CharField(max_length=500)

    def __str__(self):
        return self.user.get_full_name()