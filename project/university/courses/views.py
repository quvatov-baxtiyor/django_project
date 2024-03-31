from django.shortcuts import render, redirect
from django.http import HttpResponse

from .forms import SpecialForm, TeacherForm, SubjectForm
from .models import Special, Subject, Teacher


# Create your views here.
def index(request):
    name = request.GET.get('name')

    return HttpResponse(f"Hello {name}")


def speciality_view(request):
    search = request.GET.get('search')
    if search is None:
        specialities = Special.objects.all()
        # all_subjects = specialities.subject_set.all()
    else:
        specialities = Special.objects.filter(name__icontains=search)

        context = {'specialities': specialities}

    return render(request, 'courses/courses.html', {'specialities': specialities, 'search': search})


def subject_view(request):
    subjects = Subject.objects.all()
    return render(request, 'courses/subject_view.html', {'subjects': subjects})


def subject_detail_view(request, id):
    subject = Subject.objects.get(id=id)
    return render(request, 'courses/subject_detail_view.html', {'subject': subject})


def teacher_view(request):
    search = request.GET.get('search')
    if search is None:
        teachers = Teacher.objects.all()
    else:
        teachers = Teacher.objects.filter(first_name__icontains=search)
    return render(request, 'courses/teacher_view.html', {'teachers': teachers, 'search': search})


def speciality_create(request):
    if request.method == 'GET':
        form = SpecialForm()
    else:
        form = SpecialForm(request.POST)
        if form.is_valid():
            data = form.cleaned_data
            speciality = Special.objects.create(name=data['name'], code=data['code'], start_date=data['start_date'], is_active=data['is_active'])
            return redirect('specialities')
    return render(request, 'courses/speciality_create.html', {'form': form})

def teacher_create(request):
    if request.method == 'GET':
        form = TeacherForm()
    else:
        form = TeacherForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('teacher')
    return render(request, 'courses/teacher_create.html', {'form': form})


def subject_create(request):
    if request.method == 'GET':
        form = SubjectForm()
    else:
        form = SubjectForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('subject')
    return render(request, 'courses/subject_create.html', {'form': form})