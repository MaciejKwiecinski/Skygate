from django.urls import reverse
from django.test import TestCase

class ExamTest(TestCase):
    def exam(self):
        response = self.client.get(reverse('exam'))
        self.assertEqual(response.status_code, 200),

class ExerciseTest(TestCase):
    def exercise(self):
        response = self.client.get(reverse('exercise'))
        self.assertEqual(response.status_code, 200),

class ExerciseListTest(TestCase):
    def exam_list(self):
        response = self.client.get(reverse('exams_list'))
        self.assertEqual(response.status_code, 200),

class ExamListTest(TestCase):
    def exercise_list(self):
        response = self.client.get(reverse('exercise_list'))
        self.assertEqual(response.status_code, 200),


# Unfortunately, my tests are quite poor, because the only thing I check,
# is the returned value, and I get nothing else except status_code 200
