from . import views
from django.urls import path, include

urlpatterns = [
    path('', views.api_root),
    path('students/', views.StudentList.as_view(), name='student-list'),
    path('students/<int:pk>/', views.StudentDetail.as_view()),
    path('teachers/', views.TeacherList.as_view(), name='teacher-list'),
    path('teachers/<int:pk>/', views.TeacherDetail.as_view()),
    path('users/', views.UserList.as_view(), name = 'user-list'),
    path('users/<int:pk>/', views.UserDetail.as_view()),
]

urlpatterns += [
        path('api-auth/', include('rest_framework.urls')),
]