from django.db import models
from django.contrib.auth.models import User
from django.utils.timezone import now
# Create your models here.


class Post(models.Model):
    title = models.CharField(max_length=255)
    intro = models.TextField()
    body = models.TextField()
    date_added = models.DateTimeField(auto_now_add=True)
    blogger_name = models.ForeignKey(
        User, null=False, blank=False, on_delete=models.CASCADE, related_name="+")

    class Meta:
        ordering = ['-date_added']
