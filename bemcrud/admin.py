from django.contrib import admin
from .models import PersonModel, RequestModel

admin.site.register(PersonModel)
admin.site.register(RequestModel)