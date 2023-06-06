from django.db import models
from django.contrib.auth.models import User

# The Project model should have the following attributes:
# name - string - max_length=200
# description - string - no max_length
# owner - foreign key to the User - Refers to the auth.User model, related # # # name "projects", on delete cascade, null is True


class Project(models.Model):
    name = models.CharField(max_length=200)
    description = models.CharField(max_length=200)
    owner = models.ForeignKey(
        "auth.User",
        related_name="projects",
        on_delete=models.CASCADE,
        null=True,
    )

    def __str__(self):
        return self.name
