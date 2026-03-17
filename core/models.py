from django.db import models


class ContactMessage(models.Model):
    name = models.CharField(max_length=200)
    email = models.EmailField()
    message = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)


class SchoolInfo(models.Model):
    name = models.CharField(max_length=200)
    address = models.TextField()
    phone = models.CharField(max_length=20)
    email = models.EmailField()
    about = models.TextField()


class Slider(models.Model):
    title = models.CharField(max_length=200)
    image = models.ImageField(upload_to="slider/")
    description = models.TextField(blank=True)

    def __str__(self):
        return self.title


class PrincipalMessage(models.Model):
    name = models.CharField(max_length=200)
    message = models.TextField()
    photo = models.ImageField(upload_to="principal/")

    def __str__(self):
        return self.name
