from django.test import TestCase
from django.urls import reverse

# Create your tests here.

    def test_
        response = self.client.get(reverse('polls:index'))
        self.assertEqual(response.status_code, 200)