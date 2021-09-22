from django.contrib import admin
from .models import AssignmentFileContent, Assignment, Submission 
# Register your models here.

admin.site.register(AssignmentFileContent)
admin.site.register(Assignment)
admin.site.register(Submission)


