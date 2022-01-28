from django.test import TestCase
from django.urls import reverse

from TestingService.models import QuestionsSet, Questions, Choices


class SimpleTest(TestCase):

    def test_index(self):
        """The index page loads properly"""
        response = self.client.get('/', follow=True)
        self.assertEqual(response.status_code, 200)

    def test_details(self):
        """The Question sets list page loads properly"""
        response = self.client.get('/question_set_list/', follow=True)
        self.assertEqual(response.status_code, 200)

    def test_redirect_if_not_logged_in(self):
        response = self.client.get(reverse('TestingService:question_set_list'))
        self.assertRedirects(response, '/login/?next=/question_set_list/')


class TestViews(TestCase):
    @classmethod
    def setUpTestData(cls):
        """Creation question and answers for tests"""
        test_question = Questions.objects.create(text_question="Когда произошел третий раздел Речи Посполитой?")
        Choices.objects.create(choice="1795", flag_choice=1, question_number=test_question)
        Choices.objects.create(choice="1793", flag_choice=0, question_number=test_question)
        Choices.objects.create(choice="1792", flag_choice=0, question_number=test_question)
        test_question_2 = Questions.objects.create(
            text_question="В каком году согласно летописи произошло крещение Руси?")
        Choices.objects.create(choice="980", flag_choice=0, question_number=test_question_2)
        Choices.objects.create(choice="988", flag_choice=1, question_number=test_question_2)
        q_set = QuestionsSet.objects.create(set_title="History", id=1)
        q_set.questions.add(test_question, test_question_2)

    def test_testing_question(self):
        q_set = QuestionsSet.objects.get(pk=1)
        response = self.client.get(reverse('TestingService:test', kwargs={'pk': q_set.id}), follow=True)
        self.assertEqual(response.status_code, 200)

    def test_testing_answers_if_choose_nothing(self):
        checked_answers = []
        q_set = QuestionsSet.objects.get(pk=1)
        response = self.client.get(reverse('TestingService:testing_answers',
                                   kwargs={'pk': q_set.id}), data={'checked_ans': checked_answers}, follow=True)
        self.assertRedirects(response, '/question_set_list/1/')
