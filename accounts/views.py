from django.shortcuts import render, redirect
from . forms import LoginForm, RegisterForm
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.http import HttpResponseRedirect
from django.contrib.auth.models import User
from main.models import Course
from accounts.models import Profile


def user_login(request):
    if request.user.is_authenticated:
        return redirect('index')
    else:
        if request.method == 'POST':
            form = LoginForm(request.POST)
            if form.is_valid():
                username = form.cleaned_data['username']
                password = form.cleaned_data['password']
                user = authenticate(request, username = username, password = password)
                if user is not None:
                    if user.is_active:
                        login(request, user)
                        return redirect('index')
                    else:
                        messages.info(request, 'Account is disabled')
                else:
                    messages.info(request, 'Username or password is wrong')
        else:
            form = LoginForm()
        return render(request, 'login.html', {'form': form})

def user_register(request):

    if request.user.is_authenticated:
        return redirect('index')

    else:
        if request.method == 'POST':
            form = RegisterForm(request.POST)
            if form.is_valid():
                #new_user = form.save()
                # s         
                usuario = form.cleaned_data['username']
                email = form.cleaned_data['email']
                password = form.cleaned_data['password1']

                u = User.objects.create_user(username=usuario,email=email,password=password)
                u.save()

                #add user profile
                user_profile = Profile(user=u, username=usuario, pw = password)
                user_profile.save()
                # e
                messages.success(request, 'Account has been created, You can LOGIN')
                new_user = authenticate(username=usuario,
                                    password=password,
                                    )
                login(request, new_user)
                return redirect('index')
    
        else:
            form = RegisterForm()

        return render(request, 'register.html', {'form':form})

def user_logout(request):
    logout(request)
    return redirect('index')

def enroll_the_course(request):
    course_list = request.POST['course_list']
    if course_list:
        course = Course.objects.get(id = course_list)
        user = request.user
        course.students.add(user)

        profile = Profile.objects.get(username = user.username)
        profile.courses.add(course)
    return redirect('index')

def release_the_course(request):
    course = Course.objects.get(id = request.POST['course_id'])
    user = User.objects.get(id = request.POST['user_id'])
    course.students.remove(user)
    return redirect('index')