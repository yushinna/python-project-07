from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save


class Profile(models.Model):
    user = models.OneToOneField(
        User,
        on_delete=models.CASCADE
    )
    avatar = models.ImageField(
        upload_to='images',
        default='no-image.png',
        blank=True
    )
    first_name = models.CharField(max_length=255, default='')
    last_name = models.CharField(max_length=255, default='')
    date_of_birth = models.DateField(default='2000-12-31', blank=True)
    bio = models.TextField(default='', blank=True)
    email = models.EmailField(default='', blank=True)
    country = models.CharField(max_length=255, default='', blank=True)
    favorite_animal = models.CharField(max_length=255, default='', blank=True)
    hobby = models.CharField(max_length=255, default='', blank=True)

    def __str__(self):
        return self.user.username


def create_profile(sender, **kwargs):
    if kwargs["created"]:
        profile = Profile.objects.create(user=kwargs["instance"])
        profile.save()


post_save.connect(create_profile, sender=User)
