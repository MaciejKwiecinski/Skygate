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
    student=models.ManyToManyField(User)

    def __str__(self):
        return self.subject

class Exercise(models.Model):
    task=models.TextField()
    answers=models.TextField()
    points=models.IntegerField(default=1)
    exam = models.ForeignKey(Exam, on_delete=models.CASCADE)
