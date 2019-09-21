from django.shortcuts import render
from .models import Person as PersonModel

class Person:
  def listPerson(meta, request):
    personList = PersonModel.objects.all()
    return render(request, 'index.html', { 'personList': personList })