from django.contrib import admin
from .models import project

# Register your models here.

class ProjectAdmin(admin.ModelAdmin):
    readonly_fields = ('created', 'modified')

admin.site.register(project, ProjectAdmin)
