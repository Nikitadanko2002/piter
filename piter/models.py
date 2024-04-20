from django.contrib.auth.models import Permission
from django.db import models


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

    def __str__(self):
        return self.username


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


# class Friendship(models.Model):
#     user1 = models.ForeignKey('User', on_delete=models.CASCADE, related_name='friendships_initiated')
#     user2 = models.ForeignKey('User', on_delete=models.CASCADE, related_name='friendships_received')
#     additional_data = models.TextField()
#
#     def __str__(self):
#         return f"Friendship between {self.user1.username} and {self.user2.username}"

# class Review(models.Model):
#     RATING_CHOICES = (
#         (1, '1 star'),
#         (2, '2 stars'),
#         (3, '3 stars'),
#         (4, '4 stars'),
#         (5, '5 stars'),
#     )
#
#     rating = models.IntegerField(choices=RATING_CHOICES)
#     comment = models.TextField()
#     date = models.DateTimeField(auto_now_add=True)
#     group = models.ForeignKey('Group', on_delete=models.CASCADE, related_name='reviews')
#     event = models.ForeignKey('Event', on_delete=models.CASCADE, related_name='reviews')
#
#     def __str__(self):
#         return f"Review {self.id}"


# class Interest(models.Model):
#     name = models.CharField(max_length=255)
#     users = models.ManyToManyField('User', related_name='interests')
#
#     def __str__(self):
#         return self.name


# class Task(models.Model):
#     STATUS_CHOICES = (
#         ('todo', 'To Do'),
#         ('in_progress', 'In Progress'),
#         ('completed', 'Completed'),
#     )
#
#     name = models.CharField(max_length=255)
#     description = models.TextField()
#     status = models.CharField(max_length=20, choices=STATUS_CHOICES, default='todo')
#     group = models.ForeignKey('Group', on_delete=models.CASCADE, related_name='tasks')
#     event = models.ForeignKey('Event', on_delete=models.CASCADE, related_name='tasks')
#
#     def __str__(self):
#         return self.name
