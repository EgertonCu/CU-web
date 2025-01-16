from django.urls import path
from . import views

app_name = 'website'

urlpatterns = [
    path('', views.homepage, name='home'),
    path('ministries/', views.ministries, name='ministries'),
    path('leadership/', views.leadership, name='leadership'),
    path('about/', views.about, name='about'),
    path('privacy/', views.privacyPolicy, name='privacy'),
    path('gallery/', views.gallery, name='gallery'),
    path('contact/', views.contact, name='contact'),
    # path('blogs/', views.blogsingle, name='blogs'),
    path('library/', views.library, name='library'),
    path('register/', views.registration, name='register'),
    path('login/', views.userlogin, name='login'),
    path('forgot_password/', views.forgot_password, name='forgot'),
    path('reset_password/<str:reset_id>/', views.reset_password, name='reset'),
	path('logout/', views.logout_view, name='logout'),
	path('password-reset/<str:reset_id>/', views.password_reset_sent, name='reset-sent')


]
