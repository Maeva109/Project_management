#creation des vues API
#Ici On va maintenant créer les vues qui vont gérer les requêtes HTTP.

from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView
from projects.services.project_service import ProjectService
from projects.serializers import ProjectSerializer
from projects.models import Project

class ProjectListCreateView(APIView):
    """ Endpoint pour créer et lister les projets """

    def get(self, request):
        projects = Project.objects.all()
        serializer = ProjectSerializer(projects, many=True)
        return Response(serializer.data)

    def post(self, request):
        serializer = ProjectSerializer(data=request.data)
        if serializer.is_valid():
            project = ProjectService.create_project(
                name=serializer.validated_data['name'],
                description=serializer.validated_data.get('description', ''),
                start_date=serializer.validated_data['start_date'],
                end_date=serializer.validated_data.get('end_date', None)
            )
            return Response(ProjectSerializer(project).data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
