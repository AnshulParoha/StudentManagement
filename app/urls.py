from django.urls import path
from app.views import home,delete
urlpatterns = [
    path('',home,name='home'),
    path('update/<int:st_id>/',home,name='home'),
    path('delete/<int:st_id>/',delete,name='delete'),
]
