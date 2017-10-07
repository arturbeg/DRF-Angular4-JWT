from django.contrib import admin
from .models import Stockspecific, Orderbook
# Register your models here.

admin.site.register(Stockspecific)
admin.site.register(Orderbook)