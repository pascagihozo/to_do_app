from django.db import models
from django.contrib.auth.models import User

# Create your models here.
Priority_choices = (
    ('High', 'High'),
    ('Moderate', 'Moderate'),
    ('Low', 'Low'),

    )
class Task(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    title = models.CharField(max_length=100)
    description = models.TextField(null=True, blank=True)
    complete = models.BooleanField(default=False)
    created = models.DateTimeField(auto_now_add=True)
    priority=models.CharField(max_length=100,choices=Priority_choices, default=Priority_choices)
    

    def __str__(self):
        return self.title

    class Meta:
        ordering = ['created']


# class Priority(models.TextChoices):
    
    # def __str__(self):
    #     return self.title
    # class Meta:
    #     ordering =['high']