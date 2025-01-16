from django.urls import path
from . import views

urlpatterns = [
    path('signup/', views.signup, name='signup'),
    path('login/', views.user_login, name='login'),
    path('courses/', views.course_list, name='courses'),
     path('courses/<int:course_id>/', views.course_detail, name='course_detail'),
    path('', views.home, name='home'),
]
