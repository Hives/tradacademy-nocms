from django.http import HttpResponse
from django.shortcuts import get_object_or_404, render

from .models import Tutor, Course, DateRange


def courses_list(request):
    courses = Course.objects.all()
    return render(request, 'courses.html', {'courses': courses})


def course(request, course_slug):
    course = get_object_or_404(Course, slug=course_slug)
    dates = DateRange.objects.filter(course_id=course.id)
    return render(request, 'course.html', {'course': course, 'dates': dates})


def tutor_list(request):
    tutors = Tutor.objects.all()
    return render(request, 'tutors.html', {'tutors': tutors})


def tutor(request, tutor_slug):
    tutor = get_object_or_404(Tutor, slug=tutor_slug)
    return render(request, 'tutor.html', {'tutor': tutor})
