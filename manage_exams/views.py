from django.contrib.auth import get_user_model
from django.http import Http404
from pytz import unicode
from rest_framework.authentication import SessionAuthentication,BasicAuthentication
from rest_framework.mixins import CreateModelMixin
from rest_framework.permissions import IsAuthenticated
from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.viewsets import GenericViewSet
from .models import Exam,Exercise
from .serializers import ExamSerializer, ExerciseSerializer, RegisterSerializer


# Create your views here.

class ExamsList(APIView):
    authentication_classes = (SessionAuthentication,BasicAuthentication)

    def get(self, request, format=None):
        if request.user.is_staff == False:
            exam = Exam.objects.filter(student = request.user)
        else:
            exam = Exam.objects.all()
        serializer = ExamSerializer(exam, many=True, context={"request": request})
        return Response(serializer.data)

    def post(self, request, format=None):
        if request.user.is_staff == True:
            serializer = ExamSerializer(data=request.data)
            if serializer.is_valid():
                serializer.save()
                return Response(serializer.data, status=status.HTTP_201_CREATED)
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        else:
            return Response(status=status.HTTP_401_UNAUTHORIZED)

class ManageExamView(APIView):
    authentication_classes = (SessionAuthentication, BasicAuthentication)

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
        if request.user.is_staff == True:
            exam = self.get_object(id)
            exam.delete()
            return Response(status=status.HTTP_204_NO_CONTENT)
        else:
            return Response(status=status.HTTP_401_UNAUTHORIZED)

    def put(self,request,id, format=None):
        if request.user.is_staff == True:
            exam = self.get_object(id)
            serializer = ExamSerializer(exam, data=request.data)
            if serializer.is_valid():
                serializer.save()
                return Response(serializer.data)
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        else:
            return Response(status=status.HTTP_401_UNAUTHORIZED)

    def post(self, request, format=None):
        if request.user.is_staff == True:
            serializer = ExamSerializer(request.POST)
            if serializer.is_valid():
                serializer.save()
                return Response(serializer.data)
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        else:
            return Response(status=status.HTTP_401_UNAUTHORIZED)

class ExerciseList(APIView):
    authentication_classes = (SessionAuthentication, BasicAuthentication)

    def get(self, request, format=None):
        exercise = Exercise.objects.all()
        serializer = ExerciseSerializer(exercise, many=True, context={"request": request})
        return Response(serializer.data)

    def post(self, request, format=None):
        if request.user.is_staff == True:
            serializer = ExerciseSerializer(data=request.data)
            if serializer.is_valid():
                serializer.save()
                return Response(serializer.data, status=status.HTTP_201_CREATED)
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        else:
            return Response(status=status.HTTP_401_UNAUTHORIZED)

class ExercisesView(APIView):
    authentication_classes = (SessionAuthentication, BasicAuthentication)

    def get_object(self,id):
        try:
            return Exercise.objects.get(id=id)
        except Exercise.DoesNotExist:
            raise Http404

    def get(self, request, id, format=None):
        exercise = self.get_object(id)
        serializer = ExerciseSerializer(exercise,context={'request':request})
        return Response(serializer.data)

    def delete(self,request, id,format=None):
        if request.user.is_staff == True:
            exercise = self.get_object(id)
            exercise.delete()
            return Response(status=status.HTTP_204_NO_CONTENT)
        else:
            return Response(status=status.HTTP_401_UNAUTHORIZED)

    def put(self,request,id, format=None):
        if request.user.is_staff == True:
            exercise = self.get_object(id)
            serializer = ExerciseSerializer(exercise, data=request.data)
            if serializer.is_valid():
                serializer.save()
                return Response(serializer.data)
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        else:
            return Response(status=status.HTTP_401_UNAUTHORIZED)

    def post(self, request, format=None):
        if request.user.is_staff == True:
            serializer = ExerciseSerializer(request.POST)
            if serializer.is_valid():
                serializer.save()
                return Response(serializer.data)
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        else:
            return Response(status=status.HTTP_401_UNAUTHORIZED)

class DocsView(APIView):
    authentication_classes = (SessionAuthentication, BasicAuthentication)

    def get(self, request):
        if request.user.is_staff == True:
            apidocs = {
                   'exercises': request.build_absolute_uri('api-exercises/'),
                   'exams': request.build_absolute_uri('api-exam/'),
                   'logged users':request.build_absolute_uri('api-user/'),
                   }
        else:
            apidocs = {
                'your exams': request.build_absolute_uri('api-exam/'),
                'your account': request.build_absolute_uri('api-user/'),
            }
        return Response(apidocs)


class LoginView(APIView):
    authentication_classes = (SessionAuthentication, BasicAuthentication)
    permission_classes = (IsAuthenticated,)

    def get(self, request, format=None):
        content = {
            'user': unicode(request.user),
            'auth': unicode(request.auth),
            'admin': unicode(request.user.is_staff),
        }
        return Response(content)

class CreateUserView(CreateModelMixin, GenericViewSet):
    queryset = get_user_model().objects.all()
    serializer_class = RegisterSerializer