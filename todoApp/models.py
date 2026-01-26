from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Task(models.Model):
    user = models.ForeignKey(User,on_delete= models.CASCADE, null=False)
    task_id = models.BigAutoField(primary_key=True)
    name = models.TextField()

    def __str__(self):
        return self.name

