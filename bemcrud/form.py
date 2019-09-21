from django import forms
from .models import Person as PersonModel, Request as RequestModel

class Person(forms.ModelForm):
    class Meta:
        model = PersonModel
        fields = [
            'name',
            'cpf',
            'rg',
            'dateOfBirth',
            'telephone',
            'cellphone',
            'email',
            'cep',
            'address',
            'addressNumber',
            'state'
        ]

class Request(forms.ModelForm):
    class Meta:
        model = RequestModel
        fields = [
            'value',
            'installments'
        ]
