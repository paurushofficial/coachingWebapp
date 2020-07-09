from django.urls import path
from . import views

urlpatterns=[
    path('', views.home, name= 'Home'),
    path('courses', views.courses, name='Courses'),
    path('submitform', views.submitform , name='submitform'),
    path('home', views.home, name='Home'),
    path('form', views.form, name='Form'),
    path('downloadForm', views.downloadForm, name='DownloadForm')
]