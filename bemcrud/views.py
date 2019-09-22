from django.shortcuts import render, redirect
from decimal import Decimal

from .models import PersonModel, RequestModel
from .forms import PersonForm, RequestForm

class PersonView:

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
        RequestModel.objects.filter(cpf=person.cpf).delete()
        person.delete()
        return redirect('listPerson')

    return render(request, 'person-delete.html', {'person': person})

class RequestView:

  def create(self, request, id):
    form = RequestForm(request.POST or None)
    person = PersonModel.objects.get(id=id)

    if form.is_valid():
        prepareForm = form.save(commit=False)
        prepareForm.cpf = person.cpf
        prepareForm.save()

        return redirect('listPerson')

    return render(request, 'request-form.html', {'form': form, 'person': person })