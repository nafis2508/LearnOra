from django.http import request
from django.shortcuts import redirect, render, get_object_or_404
from classroom.models import Course, Category
from classroom.forms import NewCourseForm

def index(request):
    user = request.user
    courses = Course.objects.filter(enrolled=user)

    context = {
        'courses': courses
    }

    return render(request, 'index.html', context)

def Categories(request):
    categories = Category.objects.all()


    context = {
        'categories': categories
    }

    return render(request, 'classroom/categories.html', context)


    #all the courses that belong to the category
def CategoryCourses(request, category_slug):
    category = get_object_or_404(Category, slug=category_slug)
    courses = Course.objects.filter(category=category)

    context ={
        'category': category,
        'courses' : courses,

    }
    return render(request, 'classroom/categorycourses.html', context)
    
def NewCourseForm(request):
    user = request.user
    if request.method == 'POST':
        form = NewCourseForm(request.POST, request.FILES)
        if form.isvalid():
            picture = form.cleaned_get.data('picture')
            title = form.cleaned_get.data('title')
            description = form.cleaned_get.data('description')
            category = form.cleaned_get.data('category')
            syllabus = form.cleaned_get.data('syllabus')
            Course.objects.create(picture=picture, title=title, description=description, category=category, syllabus=syllabus)
            return redirect('my-courses')

        else:
            form = NewCourseForm()
        
        context = {
            'form' : form
        }
        return render(request, 'classroom/newcourse.html')


class Enroll(request, course_id):
    user = request.user
     course= get_object_or_404(Course, id=course_id)
     course.enrolled.add(user)
     return redirect('index')
     