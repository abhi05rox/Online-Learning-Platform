from rest_framework import generics
from .models import Course, Lesson, Student, Enrollment
from .serializers import CourseSerializer, LessonSerializer, StudentSerializer, EnrollmentSerializer

class CourseListCreate(generics.ListCreateAPIView):
    queryset = Course.objects.all()
    serializer_class = CourseSerializer

class LessonListCreate(generics.ListCreateAPIView):
    queryset = Lesson.objects.all()
    serializer_class = LessonSerializer

class StudentListCreate(generics.ListCreateAPIView):
    queryset = Student.objects.all()
    serializer_class = StudentSerializer

class EnrollmentListCreate(generics.ListCreateAPIView):
    queryset = Enrollment.objects.all()
    serializer_class = EnrollmentSerializer

class CourseRetrieveUpdateDestroy(generics.RetrieveUpdateDestroyAPIView):
    queryset = Course.objects.all()
    serializer_class = CourseSerializer

class LessonRetrieveUpdateDestroy(generics.RetrieveUpdateDestroyAPIView):
    queryset = Lesson.objects.all()
    serializer_class = LessonSerializer

class StudentRetrieveUpdateDestroy(generics.RetrieveUpdateDestroyAPIView):
    queryset = Student.objects.all()
    serializer_class = StudentSerializer

# Enrollment Views
class EnrollmentRetrieveUpdateDestroy(generics.RetrieveUpdateDestroyAPIView):
    queryset = Enrollment.objects.all()
    serializer_class = EnrollmentSerializer


from django.shortcuts import render
from django.views.generic import ListView
from .models import Course

class CourseCatalogView(ListView):
    model = Course
    template_name = 'courses/course_catalog.html'
    context_object_name = 'courses'
    paginate_by = 10  # Pagination for courses (optional)

    # Optional filtering and sorting logic
    def get_queryset(self):
        queryset = Course.objects.all()

        # Filter by title if provided
        title = self.request.GET.get('title')
        if title:
            queryset = queryset.filter(title__icontains=title)

        # Sorting by title or other fields
        sort_by = self.request.GET.get('sort_by')
        if sort_by:
            queryset = queryset.order_by(sort_by)
        return queryset


from django.views.generic import DetailView
from .models import Course

class LessonContentView(DetailView):
    model = Course  # The Course model
    template_name = 'courses/lesson_content.html'  # Path to the lesson content template
    context_object_name = 'course'  # Reference the course in the template as 'course'

    # Add the lessons to the context
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['lessons'] = self.object.lessons.all()  # Assuming 'lessons' is related to Course
        return context

from django.views.generic import DetailView
from .models import Student, Enrollment

class StudentDetailView(DetailView):
    model = Student  # The model we want to display
    template_name = 'courses/student_detail.html'  # Path to the student detail template
    context_object_name = 'student'  # Reference the student object in the template

    # Add the enrolled courses to the context
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['enrollments'] = Enrollment.objects.filter(student=self.object)  # Get courses the student is enrolled in
        return context


from django.views.generic import DetailView
from .models import Enrollment

class EnrollmentDetailView(DetailView):
    model = Enrollment
    template_name = 'courses/enrollment_detail.html'  # Template for displaying enrollment details
    context_object_name = 'enrollment'
