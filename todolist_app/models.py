from django.db import models
from django.contrib.auth.models import User 
import datetime

# Create your models here.
class TaskList(models.Model):
    manage = models.ForeignKey(User, on_delete=models.CASCADE, default=None)
    created_at = models.DateTimeField(auto_now_add=True)
    task = models.CharField(max_length=255)
    done = models.BooleanField(default=False)
    
    def __str__(self):
        return self.task + ' - ' + str(self.done)