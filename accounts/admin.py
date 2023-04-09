from django.contrib import admin
from accounts.models import Profile

admin.site.register(Profile)
class CourseAdmin(admin.ModelAdmin):
    list_display = ('name', 'available')
    list_filter = ('available', )
    search_fields = ('name', 'description')