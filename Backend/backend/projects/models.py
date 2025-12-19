from django.db import models


class Project(models.Model):
    name_pt = models.CharField(max_length=150)
    name_en = models.CharField(max_length=150)
    summary_pt = models.TextField()
    summary_en = models.TextField()
    stack = models.CharField(max_length=150)
    created_at = models.DateTimeField(auto_now_add=True)
    def __str__(self):
        return self.name_pt


class File(models.Model):
    project = models.ForeignKey(
        Project,
        related_name='files',
        on_delete=models.CASCADE
    )
    path = models.CharField(
        max_length=255,
        help_text="Ex: components/navbar"
    )
    content_pt = models.TextField()
    content_en = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    def name(self):
        return self.path.split('/')[-1]
    def __str__(self):
        return f"{self.project.name_pt} :: {self.path}"