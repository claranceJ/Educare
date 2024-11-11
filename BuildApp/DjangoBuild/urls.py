from django.urls import path

from DjangoBuild import views
urlpatterns = [
    path('', views.index, name='index'),
    path('about-us/', views.about, name='about'),
    path('blog/', views.blog, name='blog'),
    path('contact/', views.contact, name='contact'),
    path('course-details/', views.courseDetails, name='course-details'),
    path('courses/', views.courses, name='courses'),
    path('elements/', views.elements, name='elements'),
    path('single-blog/', views.singleBlog, name='single-blog'),



]