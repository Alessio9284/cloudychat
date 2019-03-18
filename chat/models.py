from django.db import models

class User(models.Model):
    nickname = models.CharField(max_length = 255)
    password = models.CharField(max_length = 32)
    color = models.CharField(max_length = 255)
    active = models.BooleanField(default = False)

class Message(models.Model):
    text = models.TextField()
    date = models.CharField(max_length=255)
    io = models.CharField(max_length=255)
    tu = models.CharField(max_length=255)