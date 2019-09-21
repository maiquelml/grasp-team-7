from django.conf.urls import url

from .views import Person

person = Person()

urlpatterns = [
    url('', person.listPerson, name='listPerson'),
]