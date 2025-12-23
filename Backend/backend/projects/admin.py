from django.contrib import admin
from .models import File, Project, ProjectAccess

@admin.register(ProjectAccess)
class ProjectAccessAdmin(admin.ModelAdmin):
    list_display = ('project', 'ip_address', 'country', 'accessed_at')
    list_filter = ('project', 'country')

admin.site.register(File)
admin.site.register(Project)