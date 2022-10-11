from django.contrib import admin
from django.urls import path, include
from get_more_done import views as todolist_views

urlpatterns = [
    path('admin/', admin.site.urls),

    path('', todolist_views.index, name='index'),
    path('todolist/', include('get_more_done.urls')),
    path('account/', include('users_app.urls')),
    path('contact', todolist_views.contact, name='contact'),
    path('about-us', todolist_views.about, name='about'),
]