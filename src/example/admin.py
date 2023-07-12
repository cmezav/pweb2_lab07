from django.contrib import admin
from .models import Simple, DateExample, NullExample

admin.site.register(Simple)
admin.site.register(DateExample)
admin.site.register(NullExample)