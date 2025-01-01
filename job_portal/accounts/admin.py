from django.contrib import admin
from .models import CustomUser, JobSeekerProfile, EmployerProfile

admin.site.register(CustomUser)
admin.site.register(JobSeekerProfile)
admin.site.register(EmployerProfile)
