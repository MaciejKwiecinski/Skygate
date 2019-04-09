"""skygate URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path,include
from manage_exams.views import ExamsList,ManageExamView,DocsView,ExerciseList,ExercisesView,LoginView
from rest_framework import routers



router = routers.DefaultRouter(trailing_slash=False)

urlpatterns = [
    path('', DocsView.as_view()),
    path('admin/', admin.site.urls),
    path('api-exam/',ExamsList.as_view(),name='exams_list'),
    path('api-exam/<int:id>',ManageExamView.as_view(),name = 'exam'),
    path('api-exercises/',ExerciseList.as_view(),name = 'exercise_list'),
    path('api-exercises/<int:id>',ExercisesView.as_view(), name = 'exercise'),
    path('api-user/',LoginView.as_view(), name = 'login' ),
    path('api-auth/', include('rest_framework.urls', namespace='rest_framework'))
]
urlpatterns += router.urls