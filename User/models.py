from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Post(models.Model):
    user = models.ForeignKey(User, on_delete=models.DO_NOTHING)
    text = models.TextField(default="")
    created_at = models.DateField()
    updated_at = models.DateField()

    def __str__(self):
        return self.text


