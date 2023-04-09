from django.contrib import admin
from . models import Course, Department

admin.site.register(Course)
class CourseAdmin(admin.ModelAdmin):
    list_display = ('name', 'available')
    list_filter = ('available', )
    search_fields = ('name', 'description')

@admin.register(Department)
class DepartmentAdmin(admin.ModelAdmin):
    prepopulated_fields={'slug':('abbreviation',)}