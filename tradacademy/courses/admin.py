from django.contrib import admin

from .models import Tutor, Venue, Course

admin.site.register(Tutor)
admin.site.register(Venue)
admin.site.register(Course)
