from django.urls import path
from app.api.views import StudentShowView,StudentCreateView,StudentUpdateDeleteView

urlpatterns = [
    path('students/',StudentShowView.as_view(),name='student_list'),
    path('students/create',StudentCreateView.as_view(),name='student_create'),
    path('students/<int:pk>',StudentUpdateDeleteView.as_view(),name='student_update_delete')
]
