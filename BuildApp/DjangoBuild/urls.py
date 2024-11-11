from django.urls import path

from DjangoBuild import views
urlpatterns = [
    path('', views.index, name='index'),
    path('about/', views.about, name='about'),
    path('blog/', views.contact, name='blog'),
    path('contact/', views.contact, name='contact'),
    path('course-details/', views.contact, name='course-details'),
    path('courses/', views.contact, name='courses'),
    path('elements/', views.contact, name='elements'),
    path('single-blog/', views.contact, name='single-blog'),



]