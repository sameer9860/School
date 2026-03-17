from django.db import models


class Class(models.Model):
    name = models.CharField(max_length=50)
    section = models.CharField(max_length=10)

    def __str__(self):
        return self.name


class Subject(models.Model):
    name = models.CharField(max_length=100)
    class_name = models.ForeignKey(Class, on_delete=models.CASCADE)

    def __str__(self):
        return self.name


class TeacherAssignment(models.Model):
    teacher = models.ForeignKey(
        "accounts.TeacherProfile",
        on_delete=models.CASCADE
    )
    subject = models.ForeignKey(Subject, on_delete=models.CASCADE)
    class_name = models.ForeignKey(Class, on_delete=models.CASCADE)


class Curriculum(models.Model):
    class_name = models.CharField(max_length=50)
    description = models.TextField()
    file = models.FileField(upload_to="curriculum/", blank=True)

    def __str__(self):
        return self.class_name
