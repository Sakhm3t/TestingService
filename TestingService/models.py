from django.db import models


# Create your models here.
from django.urls import reverse


class Questions(models.Model):
    text_question = models.CharField(max_length=200)

    class Meta:
        verbose_name = 'Questions'
        verbose_name_plural = 'Questions'

    def __str__(self):
        return str(self.text_question)


class Choices(models.Model):
    question_number = models.ForeignKey(Questions, on_delete=models.CASCADE)
    choice = models.CharField(max_length=200)
    flag_choice = models.BooleanField()

    class Meta:
        verbose_name = 'Choices'
        verbose_name_plural = 'Choices'

    def __str__(self):
        return str(self.choice)


class QuestionsSet(models.Model):
    set_title = models.TextField()
    questions = models.ManyToManyField(Questions)

    class Meta:
        verbose_name = 'QuestionsSets'
        verbose_name_plural = 'QuestionsSets'

    def __str__(self):
        return self.set_title

    def get_absolute_url(self):
        return reverse('TestingService:question_set_list', kwargs={'pk': self.pk})
