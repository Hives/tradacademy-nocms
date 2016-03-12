from django.contrib import admin

from .models import Tutor, Venue, Course, DateRange


class DateRangeInline(admin.StackedInline):
    model = DateRange
    extra = 0


class CourseAdmin(admin.ModelAdmin):
    fieldsets = [
        (None, {'fields': ['name', 'slug', 'tutor', 'venue', 'blurb']})
    ]
    inlines = [DateRangeInline]


admin.site.register(Tutor)
admin.site.register(Venue)
admin.site.register(Course, CourseAdmin)
