from rest_framework import serializers

from .models import Task


class TaskSerializer(serializers.ModelSerializer):
    class Meta:
        model = Task
        fields = (
            "id",
            "name",
            "start_date",
            "due_date",
            "is_completed",
            "project",
            "assignee",
        )
        read_only_fields = ("id",)
