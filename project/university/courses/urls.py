from django.urls import path
from .views import index, speciality_view, subject_view, teacher_view,subject_detail_view,speciality_create,teacher_create,subject_create

urlpatterns = [
    path('', index, name='index'),
    path('specialities/', speciality_view, name='specialities'),
    path('subjects/', subject_view, name='subjects'),
    path('subject/<int:id>', subject_detail_view, name='subject'),
    path('teacher/', teacher_view, name='teacher'),
    path('speciality_create/', speciality_create, name='speciality_create'),
    path('teacher_create/', teacher_create, name='teacher_create'),
    path('subject_create/',subject_create, name='subject_create')
]
