from .models import Tutor, Course


def get_menu_items(request):
    tutors = Tutor.objects.all()
    courses = Course.objects.all()

    menu_items = {
        'tutors': tutors,
        'courses': courses,
    }

    return {
        'menu_items': menu_items,
    }
