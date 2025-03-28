#definition des urls
#ici On va maintenant enregistrer ces vues

from django.urls import path
from projects.views.project_views import ProjectListCreateView
from projects.views.task_views import TaskListCreateView

urlpatterns = [
    path('projects/', ProjectListCreateView.as_view(), name='project-list-create'),
    path('tasks/', TaskListCreateView.as_view(), name='task-list-create'),
]
