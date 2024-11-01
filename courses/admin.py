from django.contrib import admin
from .models import Course


class CourseAdmin(admin.ModelAdmin):
    list_display = ('name', 'description', 'day_of_week', 'class_period')
    list_filter = ('day_of_week', 'class_period')
    search_fields = ('name',)


admin.site.register(Course, CourseAdmin)
