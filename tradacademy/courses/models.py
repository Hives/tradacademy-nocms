from django.db import models


class Tutor(models.Model):
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    slug = models.SlugField()
    pic = models.ImageField(upload_to="images/tutors")
    bio = models.TextField()

    def __str__(self):
        return u'%s %s' % (self.first_name, self.last_name)


class Venue(models.Model):
    name = models.CharField(max_length=50, blank=True)
    address_1 = models.CharField(max_length=100, blank=True)
    address_2 = models.CharField(max_length=100, blank=True)
    address_3 = models.CharField(max_length=100, blank=True)
    address_4 = models.CharField(max_length=100, blank=True)
    post_code = models.CharField(max_length=100, blank=True)

    def __str__(self):
        return self.name


class Course(models.Model):
    name = models.CharField(max_length=50, blank=True)
    slug = models.SlugField()

    tutor = models.ForeignKey(Tutor, on_delete=models.CASCADE)
    venue = models.ForeignKey(Venue, on_delete=models.CASCADE)

    blurb = models.TextField()

    def __str__(self):
        return self.name


class DateRange(models.Model):
    start_date = models.DateTimeField()
    number_of_weeks = models.IntegerField()
    course = models.ForeignKey(Course, on_delete=models.CASCADE)
