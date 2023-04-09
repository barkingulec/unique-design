from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Department(models.Model):
    name = models.CharField(max_length=50, null = True)
    abbreviation = models.CharField(max_length=8, null = True, unique = True)
    slug = models.SlugField(max_length=50, unique = True, null = True)

    def __str__(self):
        return self.name

class Course(models.Model):
    name = models.CharField(max_length=100, unique = True)
    abbreviation = models.CharField(max_length=10, null = True, unique = True)
    department = models.ForeignKey(Department, null = True, on_delete = models.DO_NOTHING)
    description = models.TextField(blank = True, null = True)
    students = models.ManyToManyField(User, blank=True, related_name='courses_joined')
    image = models.ImageField(upload_to ="courses/%Y/%m/%d", default = "images/default.png")
    available = models.BooleanField(default = True)

    def __str__(self):
        return self.name