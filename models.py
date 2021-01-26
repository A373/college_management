from django.db import models


# Create your models here.
class Student(models.Model):
    student_name = models.CharField(max_length=255)
    father_name = models.CharField(max_length=255)
    mother_name = models.CharField(max_length=255)
    date_of_birth = models.DateField()
    blood_group = models.CharField(max_length=255)
    contact_number = models.BigIntegerField()
    address = models.TextField()

    def __str__(self):
        return self.student_name


class Faculty(models.Model):
    faculty_name = models.CharField(max_length=255)
    date_of_birth = models.DateField()
    blood_group = models.CharField(max_length=255)
    contact_number = models.BigIntegerField()
    address = models.TextField()

    def __str__(self):
        return self.faculty_name


class Class(models.Model):
    branch = models.CharField(max_length=15)
    section = models.CharField(max_length=255)
    class_teacher = models.ForeignKey(Faculty, on_delete=models.SET_NULL, null=True, blank=True)
    room_no = models.IntegerField(unique=True)

    def __str__(self):
        return str(self.branch) + " | " + str(self.section)


class ClassStudent(models.Model):
    branch = models.ForeignKey(Class, on_delete=models.SET_NULL, blank=True, null=True)
    student = models.ForeignKey(Student, on_delete=models.SET_NULL, blank=True, null=True)

    def __str__(self):
        return str(self.branch) + " | " + str(self.student)


class Attendance(models.Model):
    class_student = models.ForeignKey(ClassStudent, on_delete=models.SET_NULL, blank=True, null=True)
    is_present = models.BooleanField()
    date = models.DateField()

    def __str__(self):
        return str(self.class_student) + " | " + str(self.is_present) + " | " + str(self.date)
