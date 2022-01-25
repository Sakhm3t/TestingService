import unittest

from django.test import TestCase, Client
from TestingService.models import QuestionsSet, Questions, Choices


class SimpleTest(TestCase):

    def test_index(self):
        """The index page loads properly"""
        client = Client()
        response = self.client.get('/', follow=True)
        self.assertEqual(response.status_code, 200)

    def test_details(self):
        """The Question sets list page loads properly"""
        client = Client()
        response = self.client.get('/question_set_list/', follow=True)
        self.assertEqual(response.status_code, 200)


class TestViews(TestCase):

    def setUpTestData(cls):
        pass
