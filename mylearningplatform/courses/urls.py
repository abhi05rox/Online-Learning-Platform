from django.urls import path
from . import views

urlpatterns = [
    path('courses/', views.CourseListCreate.as_view(), name='course-list-create'),
    path('lessons/', views.LessonListCreate.as_view(), name='lesson-list-create'),
    path('students/', views.StudentListCreate.as_view(), name='student-list-create'),
    path('enrollments/', views.EnrollmentListCreate.as_view(), name='enrollment-list-create'),
    path('courses/<int:pk>/', views.CourseRetrieveUpdateDestroy.as_view(), name='course-detail'),
    path('lessons/<int:pk>/', views.LessonRetrieveUpdateDestroy.as_view(), name='lesson-detail'),
    path('students/<int:pk>/', views.StudentRetrieveUpdateDestroy.as_view(), name='student-detail'),  # For retrieving, updating, and deleting a student
    path('enrollments/<int:pk>/', views.EnrollmentRetrieveUpdateDestroy.as_view(), name='enrollment-detail'),  # For retrieving, updating, and deleting an enrollment
]

