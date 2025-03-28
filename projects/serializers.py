#creation des serializers
from rest_framework import serializers
from projects.models import Project, Task, ProjectMember

class ProjectSerializer(serializers.ModelSerializer):
    class Meta:
        model = Project
        fields = '_all_'

class TaskSerializer(serializers.ModelSerializer):
    class Meta:
        model = Task
        fields = '_all_'

class ProjectMemberSerializer(serializers.ModelSerializer):
    class Meta:
        model = ProjectMember
        fields = '_all_'
