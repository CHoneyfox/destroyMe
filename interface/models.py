from django.db import models

# Create your models here.

class File(models.Model):
    destroyed_by = models.CharField(max_length=20)
    message = models.CharField(max_length=300)

    path = models.CharField(max_length=100)
    time_stamp = models.DateTimeField()

    def __str__(self):
        return self.path