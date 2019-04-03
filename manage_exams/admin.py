from django.contrib import admin
from .models import Exam,Exercise

# Register your models here.
class ExamAdmin(admin.ModelAdmin):
    list_display = ('subject','points','grades')
admin.site.register(Exam, ExamAdmin)

