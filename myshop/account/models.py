from django.db import models
from django.conf import settings
from django.contrib.auth import get_user_model


User= get_user_model()
# Create your models here.
class Profile(models.Model):
    user=models.OneToOneField(
        User,
        on_delete=models.CASCADE,
    )
    first_name= models.CharField(max_length=30, blank=True)
    last_name= models.CharField(max_length=30, blank=True)
    email = models.EmailField(max_length=254, blank=True)


    def __str__(self):
        return f'Profile of {self.user.username}'

