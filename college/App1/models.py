from django.db import models

class SigninModel(models.Model):
    email = models.EmailField(primary_key=True)
    username = models.CharField(max_length=20, unique=True, null=False)
    pas = models.CharField(max_length=10)
    cpas = models.CharField(max_length=10)
    def __str__(self):
        return self.username

class Course(models.Model):
    c_title = models.CharField(max_length=100)
    c_id = models.IntegerField(primary_key=True)
    c_name = models.CharField(unique=True, max_length=50, null=False)
    c_branch = models.CharField(null=False, max_length=50)
    c_duration = models.CharField(max_length=10, null=False)
    c_fee = models.DecimalField(max_digits=20, decimal_places=4, null=False)
    hostal = [('Available', 'Available'), ('Unavailable', 'Unavailable')]
    c_hostal = models.CharField(max_length=50, null=False, choices=hostal)
    def __str__(self):
        return self.c_name

class StudentLogin(models.Model):
    s_roll = models.IntegerField(primary_key=True)
    s_dob = models.DateField()
    s_name = models.CharField(max_length=100)
    s_course = models.ForeignKey(Course, on_delete=models.CASCADE)
    s_branch = models.CharField(max_length=50)  # Assuming branch is directly entered; you might want to derive it from Course
    s_year = models.CharField(max_length=10)
    s_address = models.TextField()
    def __str__(self):
        return self.s_name
