from django.contrib import admin
from .models import Worker, Department, Language


@admin.register(Worker)
class WorkerAdmin(admin.ModelAdmin):
    list_display = ['id', 'first_name', 'last_name', 'age', 'sex', 'department', 'language']


@admin.register(Department)
class DepartmentAdmin(admin.ModelAdmin):
    list_display = ['name', 'slug', 'floor']
    prepopulated_fields = {'slug': ('name',)}


@admin.register(Language)
class LanguageAdmin(admin.ModelAdmin):
    list_display = ['name', 'slug']
    prepopulated_fields = {'slug': ('name',)}