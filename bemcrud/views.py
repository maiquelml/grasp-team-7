from django.shortcuts import render, redirect
from decimal import Decimal

from .models import Person as PersonModel, Request as RequestModel
from .form import Person as PersonForm

class Person:
  def listPerson(meta, request):
    personList = PersonModel.objects.all()
    return render(request, 'index.html', { 'personList': personList })

  def show(meta, request, id):
    person = PersonModel.objects.get(id=id)
    requests = RequestModel.objects.filter(cpf=person.cpf) or []

    interest = 10

    if len(requests) > 0:
      for req in requests:
        normalizedRate = Decimal(interest / 100 + 1) 
        installmentsValue = (req.value * normalizedRate / req.installments)
        req.installmentsValue = round(installmentsValue, 2)

    return render(request, 'person.html', { 'person': person, 'requests': requests })

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
  
  def delete(meta, request, id):
    person = PersonModel.objects.get(id=id)

    if request.method == 'POST':
        person.delete()
        return redirect('listPerson')

    return render(request, 'person-delete.html', {'person': person})