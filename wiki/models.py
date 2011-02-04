from django.db import models

class Page(models.Model):
    name = models.CharField(max_length=200)

class Discussion(models.Model):
    tldr = models.TextField()

class Code(models.Model):
    discussion = models.ForeignKey(Discussion)
    code = models.TextField()