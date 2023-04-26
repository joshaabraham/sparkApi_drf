from django.urls import path
from . import views

urlpatterns = [
    path("schools/", views.SchoolListCreateView.as_view(), name="school_list_create"),
    path("schools/<int:pk>/", views.SchoolRetrieveUpdateDestroyView.as_view(), name="school_detail"),

    path("teachers/", views.TeacherListCreateView.as_view(), name="teacher_list_create"),
    path("teachers/<int:pk>/", views.TeacherRetrieveUpdateDestroyView.as_view(), name="teacher_detail"),

    path("students/", views.StudentListCreateView.as_view(), name="student_list_create"),
    path("students/<int:pk>/", views.StudentRetrieveUpdateDestroyView.as_view(), name="student_detail"),

    path("courses/", views.CourseListCreateView.as_view(), name="course_list_create"),
    path("courses/<int:pk>/", views.CourseRetrieveUpdateDestroyView.as_view(), name="course_detail"),

    path("sections/", views.SectionListCreateView.as_view(), name="section_list_create"),
    path("sections/<int:pk>/", views.SectionRetrieveUpdateDestroyView.as_view(), name="section_detail"),

    path("chapters/", views.ChapterListCreateView.as_view(), name="chapter_list_create"),
    path("chapters/<int:pk>/", views.ChapterRetrieveUpdateDestroyView.as_view(), name="chapter_detail"),
]