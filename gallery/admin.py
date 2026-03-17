from django.contrib import admin
from .models import GalleryCategory, GalleryImage, GalleryItem

admin.site.register(GalleryCategory)
admin.site.register(GalleryImage)
admin.site.register(GalleryItem)
