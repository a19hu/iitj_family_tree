from django.contrib import admin
from student.models import Student
from import_export.admin import ImportExportModelAdmin
from .resource import ReportResource  
class ReportAdmin(ImportExportModelAdmin):
     resource_class = ReportResource      
admin.site.register(Student, ReportAdmin)
# Register your models here.
class StudentAdmin(admin.ModelAdmin):
    save_as=True

class TreeAdmin(admin.ModelAdmin):
    save_as=True

# admin.site.register(Student,StudentAdmin)
# admin.site.register(TreeNode,TreeAdmin)
