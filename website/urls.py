from django.urls import path
from . import views

app_name = 'website'

urlpatterns = [
    path('', views.homepage, name='home'),
    path('ministries/', views.ministries, name='ministries'),
    path('leadership/', views.leadership, name='leadership'),
    path('about/', views.about, name='about'),
    path('gallery/', views.gallery, name='gallery'),
    path('contact/', views.contact, name='contact'),
    # path('blogs/', views.blogsingle, name='blogs'),
    path('library/', views.library, name='library'),
    path('register/', views.registration, name='register'),
    path('login/', views.userlogin, name='login'),
    path('reset_password/', views.password_reset, name='reset'),


]
