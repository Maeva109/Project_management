
#Service de gestion des tâches

from projects.models import Task
from django.core.exceptions import ObjectDoesNotExist

class TaskService:

    @staticmethod
    def create_task(title, description, project, assigned_to=None, due_date=None):
        """ Créer une nouvelle tâche """
        task = Task.objects.create(
            title=title,
            description=description,
            project=project,
            assigned_to=assigned_to,
            due_date=due_date
        )
        return task

    @staticmethod
    def update_task_status(task_id, new_status):
        """ Modifier le statut d'une tâche """
        try:
            task = Task.objects.get(id=task_id)
            task.status = new_status
            task.save()
            return task
        except ObjectDoesNotExist:
            return None
