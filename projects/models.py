from django.db import models


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
