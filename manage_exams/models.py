from django.db import models
from django.contrib.auth.models import User

# Create your models here.
subject={(0,'polish'),
         (1,'english'),
         (2,'PE'),
         (3,'math'),
         (4,'informatics')
         }

class Exercise(models.Model):
    task=models.TextField()
    answers=models.TextField()
    points=models.IntegerField(default=1)
    url = models.CharField(max_length= 255, default = f'0.0.0.0:8000/api-exercises/{id}')

class Exam(models.Model):
    subject=models.IntegerField(choices=subject)
    points=models.IntegerField()
    grades=models.IntegerField()
    url = models.CharField(max_length=255, default=f'0.0.0.0:8000/api-exam/{id}')
    student=models.ManyToManyField(User)
    exercise = models.ManyToManyField(Exercise)

    def __str__(self):
        return self.subject