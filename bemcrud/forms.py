from django import forms
from .models import PersonModel, RequestModel

class PersonForm(forms.ModelForm):
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

class RequestForm(forms.ModelForm):
    class Meta:
        model = RequestModel
        fields = [
            'value',
            'installments'
        ]
