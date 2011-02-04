from django.db import models
from django.contrib.auth.models import User

class Project(models.Model):
    name = models.CharField(max_length=200)

class Page(models.Model):
    name = models.CharField(max_length=200)
    tldr = models.TextField()
    last_changed = models.DateTimeField(auto_now_add=True)
    code = models.TextField()

class Discussion(models.Model):
    last_changed = models.DateTimeField(auto_now_add=True)

class Comment(models.Model):
    discussion = models.ForeignKey(Discussion)
    owner = models.OneToOneField(User)
