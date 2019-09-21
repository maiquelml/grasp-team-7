from django import forms
from .models import Person

class Person(forms.ModelForm):
    class Meta:
        model = Person
        fields = ['name', 'cpf', 'rg']
