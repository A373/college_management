from django.contrib import admin
from .models import Student, Faculty, Class, ClassStudent, Attendance


# Register your models here.

class StudentAdmin(admin.ModelAdmin):
    list_display = ['student_name', 'blood_group', 'contact_number', 'date_of_birth']
    search_fields = ['student_name', 'contact_number']


class FacultyAdmin(admin.ModelAdmin):
    list_display = ['faculty_name', 'date_of_birth', 'blood_group', 'contact_number']
    search_fields = ['faculty_name', 'contact_number']


class ClassAdmin(admin.ModelAdmin):
    list_display = ['branch', 'section', 'class_teacher', 'room_no']


class ClassStudentAdmin(admin.ModelAdmin):
    list_display = ['branch', 'student']


class AttendanceAdmin(admin.ModelAdmin):
    list_display = ['class_student', 'is_present', 'date']


admin.site.register(Student, StudentAdmin)
admin.site.register(Faculty, FacultyAdmin)
admin.site.register(Class, ClassAdmin)
admin.site.register(ClassStudent, ClassStudentAdmin)
admin.site.register(Attendance, AttendanceAdmin)
