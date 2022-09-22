from django.urls import path
from get_more_done import views

urlpatterns = [
    path('', views.todolist, name='todolist'),
    path('contact', views.contact, name='contact'),
    path('about', views.about, name='about'),
]
