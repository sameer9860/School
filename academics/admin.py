from django.contrib import admin
from .models import Class, Curriculum, Subject, TeacherAssignment

admin.site.register(Class)
admin.site.register(Subject)
admin.site.register(TeacherAssignment)
admin.site.register(Curriculum)
