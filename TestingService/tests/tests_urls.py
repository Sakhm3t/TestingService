from django.test import SimpleTestCase
from django.urls import reverse, resolve
from TestingService.views import LoginUser, logout_view, RegisterUserView, QuestionSetList, testing_question, \
    testing_answers, result_test


class TestUrls(SimpleTestCase):
    def test_LoginUser(self):
        url = reverse('TestingService:login')
        self.assertEquals(resolve(url).func.view_class, LoginUser)

    def test_logout_view(self):
        url = reverse('TestingService:logout')
        self.assertEquals(resolve(url).func, logout_view)

    def test_RegisterUserView(self):
        url = reverse('TestingService:register')
        self.assertEquals(resolve(url).func.view_class, RegisterUserView)

    def test_QuestionSetList(self):
        url = reverse('TestingService:question_set_list')
        self.assertEquals(resolve(url).func.view_class, QuestionSetList)

    def test_testing_question(self):
        url = reverse('TestingService:test', kwargs={'pk': 1})
        self.assertEquals(resolve(url).func, testing_question)

    def test_testing_answers(self):
        url = reverse('TestingService:testing_answers', kwargs={'pk': 3})
        self.assertEquals(resolve(url).func, testing_answers)

    def test_result_test(self):
        url = reverse('TestingService:result_test', kwargs={'pk': 2})
        self.assertEquals(resolve(url).func, result_test)
