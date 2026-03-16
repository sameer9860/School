from django.db import models


class Admission(models.Model):
    student_name = models.CharField(max_length=200)
    date_of_birth = models.DateField()
    class_applying = models.CharField(max_length=50)

    parent_name = models.CharField(max_length=200)
    phone = models.CharField(max_length=20)
    address = models.TextField()

    document = models.FileField(upload_to="admissions/")
    created_at = models.DateTimeField(auto_now_add=True)

    status = models.CharField(
        max_length=20,
        choices=(
            ("pending", "Pending"),
            ("approved", "Approved"),
            ("rejected", "Rejected"),
        ),
        default="pending"
    )
