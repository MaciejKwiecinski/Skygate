from django.http import Http404
from django.shortcuts import render
from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView
from .models import Exam,Exercise,User
from .serializers import ExamSerializer,UserSerializer,ExerciseSerializer

# Create your views here.

class ExamsList(APIView):

    def get(self, request, format=None):
        exams = Exam.objects.all()
        serializer = ExamSerializer(exams, many=True, context={"request": request})
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
        pass