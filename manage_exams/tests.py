from django.urls import reverse
from django.test import TestCase
from .models import User,Exam,Exercise

class Connection(TestCase):

    def exam(self):
        response = self.client.get(reverse('exam'))
        self.assertEqual(response.status_code, 200),

    def exercise(self):
        response = self.client.get(reverse('exercise'))
        self.assertEqual(response.status_code, 200),

    def exam_list(self):
        response = self.client.get(reverse('exams_list'))
        self.assertEqual(response.status_code, 200),

    def exercise_list(self):
        response = self.client.get(reverse('exercise_list'))
        self.assertEqual(response.status_code, 200),


class ModelTest(TestCase):

    def test_user(self):
        test_user = User.objects.get(id = 1)
        self.assertIsInstance(test_user, User)
        self.assertEqual(test_user.username, 'Maciej')
        self.assertEqual(test_user.is_staff, True)

    def test_exam(self):
        test_exam = Exam.objects.get(id=3)
        self.assertIsInstance(test_exam, Exam)
        self.assertEqual(test_exam.subject, 2)

    def test_exercises(self):
        test_exercises = Exercise.objects.get(id=1)
        self.assertIsInstance(test_exercises, Exercise)
        self.assertEqual(test_exercises.points, 1)
