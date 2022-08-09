from django.contrib import admin
from WebApp.models import Courses
# Register your models here.
class CourseAdmin(admin.ModelAdmin):
    list_display = ['Name','Trainer','Location','Days']
admin.site.register(Courses,CourseAdmin)