#from django.db import models

# Create your models here.
from django.contrib.auth.models import User
from django.db import models

class Project(models.Model):
    """ Modèle représentant un projet """
    name = models.CharField(max_length=255, unique=True)
    description = models.TextField(blank=True)
    start_date = models.DateField()
    end_date = models.DateField(null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def _str_(self):
        return self.name


class Task(models.Model):
    """ Modèle représentant une tâche dans un projet """
    STATUS_CHOICES = [
        ('todo', 'À faire'),
        ('in_progress', 'En cours'),
        ('done', 'Terminée'),
    ]

    title = models.CharField(max_length=255)
    description = models.TextField(blank=True)
    status = models.CharField(max_length=20, choices=STATUS_CHOICES, default='todo')
    project = models.ForeignKey(Project, on_delete=models.CASCADE, related_name="tasks")
    assigned_to = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    due_date = models.DateField(null=True, blank=True)
 
    def _str_(self):
        return self.title


class ProjectMember(models.Model):
    """ Modèle représentant l'association entre un utilisateur et un projet """
    ROLE_CHOICES = [
        ('manager', 'Manager'),
        ('developer', 'Développeur'),
        ('tester', 'Testeur'),
    ]

    user = models.ForeignKey(User, on_delete=models.CASCADE)
    project = models.ForeignKey(Project, on_delete=models.CASCADE, related_name="members")
    role = models.CharField(max_length=20, choices=ROLE_CHOICES)

    class Meta:
        unique_together = ('user', 'project')  # Un utilisateur ne peut avoir qu'un rôle par projet

    def _str_(self):
        return f"{self.user.username} - {self.project.name} ({self.role})"


