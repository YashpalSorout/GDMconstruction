from django.contrib import admin
from projects.models import Projects
class ProjectAdmin(admin. ModelAdmin):
    list_display=('project_name','project_location','client_name','project_status','work_des','start_date','end_date','project_img')
# Register your models here.

admin.site.register(Projects,ProjectAdmin)