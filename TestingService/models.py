from django.db import models


# Create your models here.

class Questions(models.Model):
    id_question = models.IntegerField(primary_key=True)
    text_question = models.CharField(max_length=200)

    class Meta:
        verbose_name = 'Questions'
        verbose_name_plural = 'Questions'

    def __str__(self):
        return str(self.id_question)


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
    id_set = models.ManyToManyField(Questions)
    set_title = models.TextField()

    def __str__(self):
        return self.set_title