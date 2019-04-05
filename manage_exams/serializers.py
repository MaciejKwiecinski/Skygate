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

class RegisterSerializer(serializers.ModelSerializer):
    password = serializers.CharField(write_only=True)

    def create(self, validated_data):
        user = User.objects.create_user(
            username=validated_data['username'],
            password=validated_data['password'],
            first_name=validated_data['first_name'],
            last_name=validated_data['last_name'],
        )
        return user

    class Meta:
        model = User
        fields = ('password', 'username', 'first_name', 'last_name',)