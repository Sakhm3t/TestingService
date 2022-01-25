from django.test import TestCase
from django.urls import reverse
from TestingService.models import QuestionsSet, Questions, Choices


class TestQuestionsSet(TestCase):
    @classmethod
    def setUpTestData(cls):
        QuestionsSet.objects.create(set_title='Химия')
        QuestionsSet.objects.create(set_title='История')

    def test_get_absolute_url(self):
        test = QuestionsSet.objects.get(id=1)
        self.assertEquals(test.get_absolute_url(), '/question_set_list/')

    def test_str(self):
        test = QuestionsSet.objects.get(id=2)
        self.assertEquals(str(test), 'История')


class TestQuestion(TestCase):
    @classmethod
    def setUpTestData(cls):
        pass