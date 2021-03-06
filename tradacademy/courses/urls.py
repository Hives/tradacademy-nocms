from django.conf.urls import url

from . import views

urlpatterns = [
    url(r'^$',
        views.courses_list,
        name="courses-courses"
        ),
    url(r'^tutors/$',
        views.tutor_list,
        name="courses-tutors"
        ),
    url(r'^tutors/(?P<tutor_slug>[\w\-]+)/$',
        views.tutor,
        name="courses-tutor"
        ),
    url(r'^(?P<course_slug>[\w\-]+)/$',
        views.course,
        name="courses-course"
        ),
]
