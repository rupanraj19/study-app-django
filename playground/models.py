from django.db import models
from datetime import datetime

class Task(models.Model):
    STATUS_CHOICES = [
        ('Pending', 'Pending'),
        ('Completed', 'Completed'),
    ]

    task = models.CharField(max_length=255)
    date = models.DateTimeField(default=datetime.now)
    status = models.CharField(max_length=10, choices=STATUS_CHOICES, default='Pending')

    def __str__(self):
        return self.task
