from django.db import models


class Exam(models.Model):
    name = models.CharField(max_length=200)
    exam_date = models.DateField()

    def __str__(self):
        return self.name


class Result(models.Model):
    student = models.ForeignKey(
        "accounts.StudentProfile",
        on_delete=models.CASCADE
    )
    subject = models.ForeignKey(
        "academics.Subject",
        on_delete=models.CASCADE
    )
    exam = models.ForeignKey(Exam, on_delete=models.CASCADE)
    marks = models.FloatField()
    grade = models.CharField(max_length=5)
