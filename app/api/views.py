from rest_framework.generics import ListAPIView,CreateAPIView,RetrieveUpdateDestroyAPIView
from app.models import Student
from .serializers import StudentSerializer


class StudentShowView(ListAPIView):
    queryset = Student.objects.all()
    serializer_class = StudentSerializer

class StudentCreateView(CreateAPIView):
    queryset = Student.objects.all()
    serializer_class = StudentSerializer

class StudentUpdateDeleteView(RetrieveUpdateDestroyAPIView):
    queryset = Student.objects.all()
    serializer_class = StudentSerializer