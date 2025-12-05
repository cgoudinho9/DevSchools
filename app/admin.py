from django.contrib import admin
from .models import *


# 2. Registre o seu Model no site de admin
admin.site.register(Curso)
admin.site.register(Plano)