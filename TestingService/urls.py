from django.urls import path

from .views import *

app_name = 'TestingService'
urlpatterns = [
    path('', main, name='main'),
    path('login/', LoginUser.as_view(), name='login'),
    path('logout/', logout_view, name='logout'),
    path('register/', RegisterUserView.as_view(), name='register'),
    path('question_set_list/', QuestionSetList.as_view(), name='question_set_list'),
    path('question_set_list/<int:pk>/', testing_question, name='test'),
    path('question_set_list/<int:pk>/answer/', testing_answers, name='testing_answers'),
    path('question_set_list/<int:pk>/result_test/', result_test, name='result_test'),

]