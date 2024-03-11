from django.contrib import admin
from .models import (
    Topu
)
# Register your models here.
@admin.register(Topu)
class TopuAdmin(admin.ModelAdmin):
    list_display = ['id','teacher_name','course_name','course_duration','seat']
    
