from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver
from django.utils import timezone


class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    is_voted = models.BooleanField(default=False)
    form = models.CharField(max_length=10)

    def __str__(self):
        return self.user.username

@receiver(post_save, sender=User)
def create_user_profile(sender, instance, created, **kwargs):
    if created:
        Profile.objects.create(user=instance)

@receiver(post_save, sender=User)
def save_user_profile(sender, instance, **kwargs):
    instance.profile.save()

class Candidat(models.Model):
    name = models.CharField(max_length=20)
    surname = models.CharField(max_length=20)
    father_name = models.CharField(max_length=20)
    bio = models.TextField()
    form = models.CharField(max_length=10)
    def __str__(self):
        full_name = ' '.join([self.surname,self.name,self.father_name])
        return full_name


class Vote(models.Model):
    voted_time = models.DateTimeField(default=timezone.now())
    user = models.OneToOneField(Profile, on_delete=models.CASCADE)
    candidat = models.ForeignKey(Candidat, on_delete=models.CASCADE)
    def __str__(self):
        return self.candidat.surname + ' ' + self.user.form


class Election(models.Model):
    start_time = models.DateTimeField()
    end_time = models.DateTimeField()
    name = models.CharField(max_length=100)
    def __str__(self):
        return self.name
