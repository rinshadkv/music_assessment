from django.db import models
from django.contrib.auth.models import User

class Music(models.Model):
    ACCESS_TYPE_CHOICES = [
        ('public', 'Public'),
        ('private', 'Private'),
        ('protected', 'Protected'),
    ]

    user = models.ForeignKey(User, on_delete=models.CASCADE)
    music_file = models.FileField(upload_to='music/')
    access_type = models.CharField(max_length=20, choices=ACCESS_TYPE_CHOICES)

    def __str__(self):
        return self.music_file.name


class AllowedEmail(models.Model):
    music = models.ForeignKey(Music, on_delete=models.CASCADE, related_name='allowed_emails')
    email = models.EmailField()

    def __str__(self):
        return self.email
