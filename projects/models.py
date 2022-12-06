from django.db import models
from django.conf import settings

# Create your models here.
class Project(models.Model):
    title = models.CharField(max_length=30)
    start_at = models.DateTimeField()
    end_at = models.DateTimeField()
    user = models.ForeignKey(
        settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name="project_user"
    )
    goal = models.CharField(max_length=50)
    skill = models.TextField()
    functions = models.TextField()


class Todo(models.Model):
    title = models.CharField(max_length=30)
    content = models.TextField()
    user = models.ForeignKey(
        settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name="todo_user"
    )
    project = models.ForeignKey(
        Project, on_delete=models.CASCADE, related_name="todo_project"
    )
    start_at = models.DateTimeField()
    end_at = models.DateTimeField()
    complete = models.IntegerField(default=0)


class Informs(models.Model):
    content = models.CharField(max_length=150)
    project = models.ForeignKey(
        Project, on_delete=models.CASCADE, related_name="info_project"
    )


class Members(models.Model):
    project = models.ForeignKey(Project, on_delete=models.CASCADE, null=True)
    user = models.CharField(max_length=100)
    leader = models.BooleanField(default=False)


class Comment(models.Model):
    project = models.ForeignKey(Project, on_delete=models.CASCADE, null=True)
    todo = models.ForeignKey(Todo, related_name="comments", on_delete=models.CASCADE)
    user = models.ForeignKey(
        settings.AUTH_USER_MODEL, related_name="comments", on_delete=models.CASCADE
    )
    parent = models.ForeignKey(
        "self", related_name="reply", on_delete=models.CASCADE, null=True, blank=True
    )
    comment = models.CharField(max_length=100)
    created_at = models.DateTimeField("생성시간", auto_now_add=True)


#
