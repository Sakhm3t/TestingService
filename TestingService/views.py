from django.contrib.auth import logout
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.views import LoginView
from django.http import HttpRequest, HttpResponse
from django.shortcuts import render, redirect

import matplotlib.pyplot as plt
import io
import base64


# Create your views here.
from django.urls import reverse_lazy
from django.views.generic import CreateView, ListView

from TestingService.forms import QuestionSetForm
from TestingService.models import QuestionsSet, Questions, Choices


def main(request):
    return render(request, 'TestingService/base.html')


def logout_view(request):
    logout(request)
    return render(request, 'TestingService/base.html')


def testing_question(request, pk):
    request.session.set_expiry(value=0)
    index = request.session.get("current_question", 0)
    q_set = Questions.objects.filter(questionsset__id=pk)
    q_number = q_set.count()
    question = q_set[index]
    answers = Choices.objects.filter(question_number=question.id)
    request.session['right_answers'] = [ans.choice for ans in
                                        Choices.objects.filter(question_number=question.id, flag_choice=1)]
    request.session['q_number'] = q_number
    data = {'question': question, 'answers': answers}
    form = QuestionSetForm(data=data)
    return render(request, 'TestingService/test_questions.html', {'form': form, 'pk': pk})


def testing_answers(request, pk):
    checked_answers = request.POST.getlist('checked_ans')
    index = request.session.get("current_question", 0)
    result = request.session.get("current_result", 0)
    # TODO: verify

    right_answers = request.session['right_answers']
    if checked_answers == right_answers:
        request.session["current_result"] = result + 1

    index += 1
    if index < request.session['q_number']:
        request.session["current_question"] = index
        return redirect("TestingService:test", pk)
    else:
        return redirect("TestingService:result_test", pk)


def result_test(request, pk):
    num = request.session.get('q_number')
    res = request.session.get("current_result")
    res = int(res)
    # построение круговой диаграммы по данным ответов
    wrong_answers = num - res
    values = [res, wrong_answers]
    labels = ['Правильно', 'Неправильно']
    colors = ['green', 'red']
    plt.pie(values, labels=labels, autopct='%1.2f%%', colors=colors, startangle=90)
    stream = io.BytesIO()
    plt.savefig(stream, format='png')
    b64str = base64.b64encode(stream.getvalue()).decode()

    data = {'res': res, 'num': num, 'b64str': b64str}
    return render(request, 'TestingService/result.html', data)


class QuestionSetList(LoginRequiredMixin, ListView):
    model = QuestionsSet
    queryset = QuestionsSet.objects.all()
    login_url = '/login/'
    template_name = 'TestingService/question_set_list.html'


class LoginUser(LoginView):
    template_name = 'TestingService/login.html'
    form_class = AuthenticationForm

    def get_success_url(self):
        return reverse_lazy('TestingService:question_set_list')


class RegisterUserView(CreateView):
    form_class = UserCreationForm
    template_name = 'TestingService/register.html'
    success_url = reverse_lazy('TestingService:login')
