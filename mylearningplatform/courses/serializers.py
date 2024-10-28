from rest_framework import serializers
from .models import Course, Lesson, Student, Enrollment

class CourseSerializer(serializers.ModelSerializer):
    class Meta:
        model = Course
        fields = '__all__'

class StudentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Student
        fields = '__all__'

class EnrollmentSerializer(serializers.ModelSerializer):
    # Custom fields to display the student's full name and course title
    student_name = serializers.SerializerMethodField(read_only=True)  # Display full student name
    course_title = serializers.CharField(source='course.title', read_only=True)  # Display course title
    enrolled_at = serializers.SerializerMethodField()  # Custom method for formatting datetime

    # Use PrimaryKeyRelatedField to handle student and course IDs during creation
    student = serializers.PrimaryKeyRelatedField(queryset=Student.objects.all(), write_only=True)
    course = serializers.PrimaryKeyRelatedField(queryset=Course.objects.all(), write_only=True)

    class Meta:
        model = Enrollment
        fields = ['id', 'enrolled_at', 'progress', 'student', 'course', 'student_name', 'course_title']

    # Custom method to concatenate the first name and last name of the student
    def get_student_name(self, obj):
        return f"{obj.student.first_name} {obj.student.last_name}"
    
    def get_enrolled_at(self, obj):
        # Format the date to 'YYYY-MM-DD' and time to 'HH:MM:SS'
        return obj.enrolled_at.strftime('%Y-%m-%d %H:%M:%S')
    

# class EnrollmentSerializer(serializers.ModelSerializer):
#     student = serializers.SerializerMethodField()
#     course = serializers.SerializerMethodField()
#     enrolled_at = serializers.SerializerMethodField()  # Custom method for formatting datetime

#     class Meta:
#         model = Enrollment
#         fields = ['id', 'student', 'course', 'progress', 'enrolled_at']

#     def get_student(self, obj):
#         return f"{obj.student.first_name} {obj.student.last_name}"

#     def get_course(self, obj):
#         return obj.course.title

#     def get_enrolled_at(self, obj):
#         # Format the date to 'YYYY-MM-DD' and time to 'HH:MM:SS'
#         return obj.enrolled_at.strftime('%Y-%m-%d %H:%M:%S')



class LessonSerializer(serializers.ModelSerializer):
    class Meta:
        model = Lesson
        fields = '__all__'