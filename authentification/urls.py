from django.urls import path
from . import views

urlpatterns = [
    path('signup/',view=views.signup, name='signup'),
    path('login/',view=views.user_login, name='login'),
    path('logout/',view=views.user_logout, name='logout'),
    path('',view=views.index, name='index'),

]