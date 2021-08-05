from django import forms
from django.forms import fields, widgets
from survey.models import Survey


class SurveyForm(forms.ModelForm):
    class Meta:
        model = Survey
        fields = ('gender', 'age')
        widgets = {
            'result': forms.HiddenInput(),
            'audio_path': forms.HiddenInput()
        }
