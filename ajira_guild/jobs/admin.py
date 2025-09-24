from django.contrib import admin
from .models import Job, Application, JobCategory

admin.site.register(Job)
admin.site.register(Application)
admin.site.register(JobCategory)
