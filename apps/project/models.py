from django.db import models

# Creamos nuestro modelo
class Project(models.Model):
    image = models.ImageField(upload_to="project/")
    title = models.CharField(max_length=50)
    description = models.TextField(max_length=100)
    url = models.URLField()

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = "Project"
        verbose_name_plural = "Project's"