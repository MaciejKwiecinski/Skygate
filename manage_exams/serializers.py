from django.contrib.auth.models import User
from rest_framework import serializers
from .models import Exercise,Exam


class ExamSerializer(serializers.ModelSerializer):
    grades = serializers.IntegerField(min_value=1,max_value=6)
    class Meta:
        model=Exam
        fields=('subject','points','student','grades',"exercise",'url')

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('username','first_name','last_name')

class ExerciseSerializer(serializers.ModelSerializer):
    class Meta:
        model=Exercise
        fields = ('task','answers','points','url',)