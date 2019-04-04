from django.http import Http404
from rest_framework.authentication import SessionAuthentication,BasicAuthentication
from rest_framework.permissions import IsAdminUser
from rest_framework.decorators import permission_classes,api_view
from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView
from .models import Exam,Exercise,User
from .serializers import ExamSerializer,ExerciseSerializer,UserSerializer

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
            pass

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

    @permission_classes((IsAdminUser,))
    def delete(self,request, id,format=None):
        exam = self.get_object(id)
        exam.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

    @permission_classes((IsAdminUser,))
    def put(self,request,id, format=None):
        exam = self.get_object(id)
        serializer = ExamSerializer(exam, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    @permission_classes((IsAdminUser,))
    def post(self, request, id, format=None):
        serializer = ExamSerializer(request.POST)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class ExerciseList(APIView):
    authentication_classes = (SessionAuthentication, BasicAuthentication)

    def get(self, request, format=None):
        exercise = Exercise.objects.all()
        serializer = ExerciseSerializer(exercise, many=True, context={"request": request})
        return Response(serializer.data)

    @permission_classes((IsAdminUser,))
    def post(self, request, format=None):
        serializer = ExerciseSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

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

    @permission_classes((IsAdminUser,))
    def delete(self,request, id,format=None):
        exercise = self.get_object(id)
        exercise.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

    @permission_classes((IsAdminUser,))
    def put(self,request,id, format=None):
        exercise = self.get_object(id)
        serializer = ExerciseSerializer(exercise, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    @permission_classes((IsAdminUser,))
    def post(self, request, id, format=None):
        serializer = ExerciseSerializer(request.POST)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class DocsView(APIView):
    authentication_classes = (SessionAuthentication, BasicAuthentication)

    def get(self, request):
        if request.user.is_staff == True:
            apidocs = {
                   'exercises': request.build_absolute_uri('api-exercises/'),
                   'exams': request.build_absolute_uri('api-exam/'),
                   }
        else:
            apidocs = {
                'your exams': request.build_absolute_uri('api-exam/'),
            }
        return Response(apidocs)

@api_view(['POST'])
def create_auth(request):
    serialized = UserSerializer(data=request.data)
    if serialized.is_valid():
        User.objects.create_user(
            serialized.init_data['email'],
            serialized.init_data['username'],
            serialized.init_data['password']
        )
        return Response(serialized.data, status=status.HTTP_201_CREATED)
    else:
        return Response(serialized._errors, status=status.HTTP_400_BAD_REQUEST)