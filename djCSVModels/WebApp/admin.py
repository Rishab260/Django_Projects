from django.contrib import admin
from WebApp.models import Employee
# Register your models here.
class EmpAdmin(admin.ModelAdmin):
    list_display = ['eid','ename','eloc']
admin.site.register(Employee,EmpAdmin)