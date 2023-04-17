from . import views
from django.urls import path, include

urlpatterns = [
    path('', views.StudentList.as_view(), name='students'),
    path('<int:pk>/', views.StudentDetail.as_view()),
    path('teachers/', views.TeacherList.as_view(), name='teacher-list'),
    path('teachers/<int:pk>/', views.TeacherDetail.as_view()),
]