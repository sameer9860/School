from django.contrib import admin
from .models import ContactMessage, PrincipalMessage, SchoolInfo, Slider

admin.site.register(ContactMessage)
admin.site.register(Slider)
admin.site.register(PrincipalMessage)
admin.site.register(SchoolInfo)
