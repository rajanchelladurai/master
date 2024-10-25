from django.db import models

# Create your models here.
class Event(models.Model):
    title = models.CharField(max_length =200)
    description = models.TextField(blank=True)
    start_date = models.DateTimeField()
    end_date = models.DateTimeField()

    def __str__(self):
        return self.title