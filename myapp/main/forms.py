from django import forms
from main.models import Update

class UpdateForm(forms.ModelForm):
    update = forms.IntegerField(widget=forms.HiddenInput())

    class Meta:
        model = Update
        fields = ('update',)