from django.contrib import admin
from .models import Place, Symbol
from . models import Meettheteam
# from . models import Symbol

# Register your models here.
admin.site.register(Place)

admin.site.register(Meettheteam)

admin.site.register(Symbol)