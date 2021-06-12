from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Confession(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    title = models.CharField(max_length=255)
    text = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    likes = models.ManyToManyField(User, related_name='confessions', blank=True)

    def total_likes(self):
        return self.likes.count()

    def __str__(self):
        return self.title + ' - ' + self.user.username