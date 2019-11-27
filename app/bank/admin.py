from django.contrib import admin
from bank.models import Branch, Customer

admin.site.register((Branch, Customer))
