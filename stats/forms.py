from django import forms
from django.forms import ModelForm
from .models import Match, MatchResults


class MatchForm(ModelForm):
    class Meta:
        model = Match
        fields = '__all__'


class MatchResultsForm(ModelForm):
    class Meta:
        model = MatchResults
        fields = '__all__'
