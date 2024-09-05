from django.urls import path
from . import views

urlpatterns = [
    path("schoolsCreate/", views.SchoolListCreateView.as_view(), name="school_create"),
    path("schools/<int:pk>/", views.SchoolRetrieveUpdateDestroyView.as_view(), name="school_detail"),

    path("teachersCreate/", views.TeacherListCreateView.as_view(), name="teacher_create"),
    path("teachers/<int:pk>/", views.TeacherRetrieveUpdateDestroyView.as_view(), name="teacher_detail"),

    path("studentsCreate/", views.StudentListCreateView.as_view(), name="student_create"),
    path("students/<int:pk>/", views.StudentRetrieveUpdateDestroyView.as_view(), name="student_detail"),

    path("coursesCreate/", views.CourseListCreateView.as_view(), name="course_create"),
    path("courses/<int:pk>/", views.CourseRetrieveUpdateDestroyView.as_view(), name="course_detail"),

    path("sectionsCreate/", views.SectionListCreateView.as_view(), name="section_create"),
    path("sections/<int:pk>/", views.SectionRetrieveUpdateDestroyView.as_view(), name="section_detail"),

    path("chaptersCreate/", views.ChapterListCreateView.as_view(), name="chapter_create"),
    path("chapters/<int:pk>/", views.ChapterRetrieveUpdateDestroyView.as_view(), name="chapter_detail"),
]