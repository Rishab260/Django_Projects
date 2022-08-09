from django.contrib import admin
from WebApp.models import Student
# Register your models here.
class StudentAdmin(admin.ModelAdmin):
    list_display = ['stdno','stdname','stdmarks','stdresult']
admin.site.register(Student,StudentAdmin)