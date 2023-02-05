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


class PlayerForm(forms.Form):
    player_name = forms.CharField(label='Enter player name:', max_length=100)
