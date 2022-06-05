from django.contrib import admin
from .models import Hermanos, Padres, Tios

# Register your models here.

admin.site.register(Hermanos)
admin.site.register(Padres)
admin.site.register(Tios)

