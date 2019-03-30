from django.contrib.auth.models import User
from rest_framework import serializers
from .models import Exercise,Exam

class ExamSerializer(serializers.HyperlinkedModelSerializer):
    grades=serializers.IntegerField(min_value=1,max_value=6)
    class Meta:
        model=Exam
        fields=('subject','points','student')

class UserSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = User
        fields = ('id', 'username','first_name','last_name')

class ExerciseSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model=Exercise
        fields = '__all__'
