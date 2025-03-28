
##ici on implimente la gestion des projet,Service de gestion des projets

from projects.models import Project, ProjectMember
from django.core.exceptions import ObjectDoesNotExist

class ProjectService:

    @staticmethod
    def create_project(name, description, start_date, end_date):
        """ Créer un nouveau projet """
        project = Project.objects.create(
            name=name,
            description=description,
            start_date=start_date,
            end_date=end_date
        )
        return project

    @staticmethod
    def get_project_by_id(project_id):
        """ Récupérer un projet par son ID """
        try:
            return Project.objects.get(id=project_id)
        except ObjectDoesNotExist:
            return None

    @staticmethod
    def add_member_to_project(project, user, role):
        """ Ajouter un membre à un projet """
        member, created = ProjectMember.objects.get_or_create(
            project=project, 
            user=user,
            defaults={'role': role}
        )
        return member
    