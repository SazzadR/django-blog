from django.db import models
from django.contrib.auth.models import AbstractUser


class User(AbstractUser):
    class Meta(object):
        unique_together = ['email']


class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    image = models.ImageField(default=None, upload_to='profile_pics', null=True)

    def __str__(self):
        return '{} Profile'.format(self.user)
