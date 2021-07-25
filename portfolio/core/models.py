from django.db import models
from ckeditor.fields import RichTextField

# Create your models here.



class project(models.Model):
    title = models.CharField(max_length=200)
    subtitle = models.CharField(max_length=200)
    url = models.CharField(max_length=200, null= True)
    content = RichTextField()
    image = models.ImageField(upload_to="projects")
    created = models.DateTimeField(auto_now_add=True)
    modified = models.DateTimeField(auto_now=True)

    class Meta:
            verbose_name = "project"
            verbose_name_plural = "projects"
            ordering = ['-created']

    def __str__(self):
        return self.title
