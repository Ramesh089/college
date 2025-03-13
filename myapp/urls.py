from django.urls import path
from . import views

urlpatterns = [
    path('signup/', views.signup_view, name='signup'),
    path('login/', views.login_view, name='login'),
    path('', views.home, name='home'),
    path('about/', views.about, name='about'),
    path('report/', views.report, name='report'),
    # path('quize/', views.quize, name='quize'),
    path('contact/', views.contact, name='contact'),

]

