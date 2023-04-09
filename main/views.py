from django.shortcuts import render
from . models import Department, Course
from accounts.models import Profile

def index(request):
    courses = Course.objects.all().order_by('name')
    departments = Department.objects.all().order_by('name')

    context = {
        'courses': courses,
        'departments': departments,
    }
    
    if request.user.is_authenticated:
        profile = Profile.objects.get(username = request.user.username)
        enrolled_courses = profile.courses.order_by('name')
        context['enrolled_courses'] = enrolled_courses
        context['is_enrolled'] = len(enrolled_courses.all()) > 0

    return render(request, 'index.html', context)

def course_detail(request, course_id):
    course = Course.objects.get(id = course_id)
    context = {
        'course': course,
    }
    return render(request, "course.html", context)
