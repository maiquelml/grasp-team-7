from django.urls import path
from django.conf import settings
from django.conf.urls.static import static

from .views import Person, Request

person = Person()
request = Request()

urlpatterns = [
    path('excluir-pessoa/<int:id>/', person.delete, name='deletePerson'),
    path('editar-pessoa/<int:id>/', person.update, name='updatePerson'),
    path('incluir-pessoa', person.create, name='createPerson'),
    path('incluir-proposta/<int:id>', request.create, name='createRequest'),
    path('pessoa/<int:id>', person.show, name='showPerson'),
    path('', person.listPerson, name='listPerson'),
] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)