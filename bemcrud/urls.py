from django.conf import settings
from django.conf.urls.static import static
from django.urls import path

from .views import Person

person = Person()

urlpatterns = [
    path('incluir-pessoa', person.create, name='create'),
    path('', person.listPerson, name='listPerson'),
] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)