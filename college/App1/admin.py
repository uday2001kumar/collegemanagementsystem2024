from django.contrib import admin
from .models import SigninModel,Course,StudentLogin
# Register your models here.
class SigninAdminModel(admin.ModelAdmin):
    list_display=['email','username','pas','cpas']
admin.site.register(SigninModel,SigninAdminModel)
class CourseAdmin(admin.ModelAdmin):
    list_display=['c_id','c_name','c_branch','c_duration','c_fee']
admin.site.register(Course,CourseAdmin)
class StudentLoginAdmin(admin.ModelAdmin):
    list_display=['s_roll','s_dob']
admin.site.register(StudentLogin,StudentLoginAdmin)
