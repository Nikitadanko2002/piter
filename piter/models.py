from django.db import models
from django.contrib.auth.models import AbstractUser, Permission
from django.contrib.auth.models import Permission
from django.db import models
from django.urls import reverse

# class Event(models.Model):
#     title = models.CharField(max_length=255)
#     description = models.TextField()
#     start_date = models.DateTimeField()
#     end_date = models.DateTimeField()
#     location = models.CharField(max_length=255)
#     attendees = models.ManyToManyField('User', related_name='events_attending')
#     organizer = models.ForeignKey('User', on_delete=models.CASCADE, related_name='events_organizing')
#
#     def __str__(self):
#         return self.title




class Location(models.Model):
    name = models.CharField(max_length=255)
    address = models.CharField(max_length=255)
    coordinates = models.CharField(max_length=255)
    additional_info = models.TextField()

    def __str__(self):
        return self.name


class User(models.Model):
    avatar = models.ImageField(upload_to='avatars/', null=True, blank=True)
    first_name = models.CharField(max_length=255)
    second_name = models.CharField(max_length=255)
    bio = models.TextField(null=True, blank=True)
    friends = models.ManyToManyField('self', blank=True)
    user_permissions = models.ManyToManyField(Permission, blank=True, related_name='user_permission_users')

    # def get_absolute_url(self):
    #     return reverse('profile', kwargs={'pk': self.pk})
    def __str__(self):
        return self.first_name


class Group(models.Model):
    name = models.CharField(max_length=255)
    description = models.TextField()
    size = models.IntegerField()
    members = models.ManyToManyField(User, related_name='groups_joined')

    def __str__(self):
        return self.name


class Event(models.Model):
    title = models.CharField(max_length=255)
    description = models.TextField()
    start_date = models.DateTimeField()
    end_date = models.DateTimeField()
    location = models.OneToOneField(Location, on_delete=models.CASCADE)

    organizer = models.ForeignKey(Group, on_delete=models.CASCADE, related_name='events_organizing')

    def __str__(self):
        return self.title


class Category(models.Model):
    title = models.CharField(max_length=255)
    event = models.ForeignKey(Event, on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)