from django.db import models
from django.contrib.auth.models import User

# Create your models here.
subject={(0,'polish'),
         (1,'english'),
         (2,'PE'),
         (3,'math'),
         (4,'informatics')
         }

class Exam(models.Model):
    subject=models.IntegerField(choices=subject)
    points=models.IntegerField()
    grades=models.IntegerField()
    student=models.OneToOneField(User, on_delete=models.CASCADE, primary_key=True)

class Exercise(models.Model):
    task=models.TextField()
    answers=models.TextField()
    exam = models.ForeignKey(Exam, on_delete=models.CASCADE)
