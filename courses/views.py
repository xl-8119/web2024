from django.shortcuts import render
from django.shortcuts import render, redirect
from .models import Course
from django.contrib.auth.decorators import login_required


@login_required
def course_list(request):
    courses = Course.objects.exclude(students=request.user)
    return render(request, 'courses/course_list.html', {'courses': courses})


@login_required
def enroll_course(request, course_id):
    course = Course.objects.get(id=course_id)
    course.students.add(request.user)
    return redirect('my_courses')


@login_required
def my_courses(request):
    # 提取当前用户的课程并按周几和节次组织
    courses = request.user.courses.all()
    schedule = {}

    for course in courses:
        day = course.day_of_week
        period = course.class_period
        if day not in schedule:
            schedule[day] = {}
        # 将课程转换为字典形式，以便 JSON 序列化
        schedule[day][period] = {
            'name': course.name,
            'description': course.description,
        }

    # 定义周几和节次对应的时间范围
    days_of_week = [1, 2, 3, 4, 5, 6, 7]  # 周一到周日
    period_times = {
        1: "8:00 - 10:00",
        2: "10:00 - 12:00",
        3: "14:00 - 16:00",
        4: "16:00 - 18:00"
    }

    return render(request, 'courses/my_courses.html', {
        'schedule': schedule,
        'days_of_week': days_of_week,
        'period_times': period_times
    })
