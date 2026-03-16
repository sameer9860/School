from django.contrib.auth.models import AbstractUser
from django.db import models


class User(AbstractUser):

    ROLE_CHOICES = (
        ("admin", "Admin"),
        ("teacher", "Teacher"),
        ("student", "Student"),
        ("parent", "Parent"),
    )

    role = models.CharField(max_length=20, choices=ROLE_CHOICES)
    phone = models.CharField(max_length=20, blank=True)


class StudentProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    class_name = models.CharField(max_length=50)
    roll_number = models.IntegerField()
    date_of_birth = models.DateField()
    address = models.TextField()


class TeacherProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    qualification = models.CharField(max_length=200)
    subject = models.CharField(max_length=100)
    photo = models.ImageField(upload_to="teachers/")