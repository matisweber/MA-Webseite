from django.urls import path, include
from . import views


urlpatterns = [
    path('', views.home, name="home"),
    path('course', views.course, name='course'),
    path('home', views.home, name="home"),
    path('coursecreate', views.coursecreate, name="coursecreate"),
    path('showcourse/<course_id>', views.showcourse, name="showcourse"),
    path('searchcourse', views.searchcourse, name="searchcourse"),
]
