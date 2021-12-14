from django.shortcuts import render, redirect
from django.http import HttpResponse
from .forms import CourseForm
from django.contrib import messages
from .models import Course

# Create your views here.

def home(request):
    #all_members = Members.objects.all
    return render(request, "index.html", {})#'all': all_members})

def course(request):
    course_list = Course.objects.all()
    return render(request, "course.html", {'course': course_list})



    

def coursecreate(request):
    if request.method == "POST":
        form = CourseForm(request.POST or None)
        if form.is_valid():
            form.save()
        messages.success(request, ('You have creatd your course successfully!'))
        return redirect('home')
    else:
        return render(request, 'coursecreate.html', {})





def showcourse(request, course_id):
    showcourse_list = Course.objects.get(pk=course_id)
    return render(request, "showcourse.html", {'course': showcourse_list})

def searchcourse(request):
    if request.method == "POST":
        searched = request.POST['searched']
        #courses = Course.objects.filter(name__contains=searched)
        courses = Course.objects.filter(language__contains=searched)
        return render(request, 'searchcourse.html', {'searched':searched,'courses':courses})

    else:
        return render(request, 'searchcourse.html', {})



