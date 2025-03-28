
from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView
from projects.services.task_service import TaskService
from projects.serializers import TaskSerializer
from projects.models import Task

class TaskListCreateView(APIView):
    """ Endpoint pour créer et lister les tâches """

    def get(self, request):
        tasks = Task.objects.all()
        serializer = TaskSerializer(tasks, many=True)
        return Response(serializer.data)

    def post(self, request):
        serializer = TaskSerializer(data=request.data)
        if serializer.is_valid():
            task = TaskService.create_task(
                title=serializer.validated_data['title'],
                description=serializer.validated_data.get('description', ''),
                project=serializer.validated_data['project'],
                assigned_to=serializer.validated_data.get('assigned_to', None),
                due_date=serializer.validated_data.get('due_date', None)
            )
            return Response(TaskSerializer(task).data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
