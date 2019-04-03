from django.http import Http404
import django_filters.rest_framework
from django.shortcuts import render
from django.views import View
from rest_framework import status, generics, mixins, viewsets
from rest_framework.response import Response
from rest_framework.views import APIView
from django.contrib.auth.models import User
from .models import Exam,Exercise
from .serializers import ExamSerializer,UserSerializer,ExerciseSerializer

# Create your views here.

class ExamsList(APIView):

    def get(self, request, format=None):
        exam = Exam.objects.all()
        serializer = ExamSerializer(exam, many=True, context={"request": request})
        return Response(serializer.data)

    def post(self, request, format=None):
        serializer = ExamSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class ManageExamView(APIView):
    def get_object(self,pk):
        try:
            return Exam.objects.get(pk=pk)
        except Exam.DoesNotExist:
            raise Http404

    def get(self, request, id, format=None):
        exam = self.get_object(id)
        serializer = ExamSerializer(exam,context={'request':request})
        return Response(serializer.data)

    def delete(self,request, id,format=None):
        exam = self.get_object(id)
        exam.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

    def put(self,request,id, format=None):
        exam = self.get_object(id)
        serializer = ExamSerializer(exam, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def post(self, request, id, format=None):
        serializer = ExamSerializer(request.POST)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class ExerciseList(APIView):

    def get(self, request, format=None):
        exercise = Exercise.objects.all()
        serializer = ExerciseSerializer(exercise, many=True, context={"request": request})
        return Response(serializer.data)

    def post(self, request, format=None):
        serializer = ExerciseSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class ExercisesView(APIView):
    def get_object(self,pk):
        try:
            return Exercise.objects.get(pk=pk)
        except Exercise.DoesNotExist:
            raise Http404

    def get(self, request, id, format=None):
        exercise = self.get_object(id)
        serializer = ExerciseSerializer(exercise,context={'request':request})
        return Response(serializer.data)

    def delete(self,request, id,format=None):
        exercise = self.get_object(id)
        exercise.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

    def put(self,request,id, format=None):
        exercise = self.get_object(id)
        serializer = ExerciseSerializer(exercise, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def post(self, request, id, format=None):
        serializer = ExerciseSerializer(request.POST)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class DocsView(APIView):

    def get(self, request, *args, **kwargs):
        apidocs = {
                   'exercises': request.build_absolute_uri('api-exercises/'),
                   'exams': request.build_absolute_uri('api-exam/'),
                   }
        return Response(apidocs)