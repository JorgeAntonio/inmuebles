from django.contrib import admin
from .models import Comentario, Edificacion, Empresa

# Register your models here.

admin.site.register(Edificacion)
admin.site.register(Empresa)
admin.site.register(Comentario)
