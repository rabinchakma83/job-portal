from django.contrib import admin
from .models import User, RecruiterProfile, JobSeekerProfile

# Register your models here.
admin.site.register(User)
admin.site.register(RecruiterProfile)
admin.site.register(JobSeekerProfile)
