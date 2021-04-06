from django.contrib.auth.models import AbstractUser
from django.db import models

class CustomUser(AbstractUser):
    avatar = models.ImageField(upload_to='avatar', blank=True, null=True, default='avatar/default_user.png')
    date_of_birth = models.DateField(null=True, blank=True)
    class Meta:
        db_table = 'auth_user'