from django.shortcuts import render
from .models import Person

def listPerson(request):
  personList = Person.objects.all()
  return render(request, 'index.html', { 'personList': personList })