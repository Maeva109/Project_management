from django.contrib import admin

# Register your models here.
#Ajouter les modeles a ladmin django
#Pour tester rapidement les modèles

from django.contrib import admin
from .models import Project, Task, ProjectMember

admin.site.register(Project)
admin.site.register(Task)
admin.site.register(ProjectMember)

