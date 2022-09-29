from django.contrib import admin
from django.urls import path, include
from get_more_done import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.index, name='index'),
    path('todolist/', include('get_more_done.urls')),
    path('contact', views.contact, name='contact'),
    path('about', views.about, name='about'),
]
