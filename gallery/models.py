from django.db import models


class GalleryCategory(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name


class GalleryImage(models.Model):
    title = models.CharField(max_length=200)
    category = models.ForeignKey(
        GalleryCategory,
        on_delete=models.CASCADE
    )
    image = models.ImageField(upload_to="gallery/")
    uploaded_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title
