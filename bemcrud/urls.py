from django.conf.urls import url

from .views import listPerson

urlpatterns = [
    url('', listPerson, name='listPerson'),
]