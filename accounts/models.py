from django.db import models
from django.contrib.auth.models import User
from main.models import Course

class Profile(models.Model):
    user = models.OneToOneField(User, null = True, on_delete = models.CASCADE)
    username = models.CharField(null = True, max_length=50)
    pw = models.CharField(null = True, max_length=50)
    courses = models.ManyToManyField(Course, blank=True, related_name='users_courses')
    first_name = models.CharField(null = True, blank = True, max_length = 100)
    last_name = models.CharField(null = True, blank = True, max_length = 100)
    description = models.TextField(blank=True)
    image = models.ImageField(default="images/default.png",upload_to="profiles/%Y/%m/%d/")
    thumbnail = models.ImageField(default="/images/thumbnail.png",upload_to="profiles/%Y/%m/%d/")
    facebook = models.URLField(max_length=100, null = True, blank=True)
    twitter = models.URLField(max_length=100, null = True, blank=True)
    instagram = models.URLField(max_length=100, null = True, blank=True)
    youtube = models.URLField(max_length=100, null = True, blank=True)

    def __str__(self):
        return str(self.username)