from django import forms
from .models import *


class QuestionSetForm(forms.Form):
    question = forms.CharField(
        max_length=500,
        label='Вопрос ',
        widget=forms.Textarea(attrs={'rows': 3, 'cols': 30, 'readonly': True})
    )
    answers = forms.ModelMultipleChoiceField(
        queryset=None,
        widget=forms.CheckboxSelectMultiple(),
        label='Варианты ответа'
    )

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['answers'].queryset = kwargs['data']['answers']
