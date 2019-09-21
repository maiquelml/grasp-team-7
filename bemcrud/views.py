from django.shortcuts import render, redirect
from .models import Person as PersonModel
from .form import Person as PersonForm

class Person:
  def listPerson(meta, request):
    personList = PersonModel.objects.all()
    return render(request, 'index.html', { 'personList': personList })

  def create(meta, request):
    form = PersonForm(request.POST or None)

    if form.is_valid():
        form.save()
        return redirect('listPerson')

    return render(request, 'person-form.html', {'form': form})

  def update(meta, request, id):
    person = PersonModel.objects.get(id=id)
    form = PersonForm(request.POST or None, instance=person)

    if form.is_valid():
        form.save()
        return redirect('listPerson')

    return render(request, 'person-form.html', {'form': form, 'person': person})