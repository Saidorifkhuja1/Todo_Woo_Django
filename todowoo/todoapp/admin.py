
from django.contrib import admin
from .models import Task

@admin.register(Task)
class TaskAdmin(admin.ModelAdmin):
    list_display = ['title', 'description', 'completed', 'created_at', 'updated_at', 'user']
    list_filter = ['completed', 'user']
    search_fields = ['title', 'description']
