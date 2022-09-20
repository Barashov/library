from django.urls import path
from django.contrib.auth.views import LogoutView
from .views import *
urlpatterns = [
    path('signup', UserCreateView.as_view(), name='signup'),
    path('login/', UserLoginView.as_view(), name='login'),
    path('logout/', LogoutView.as_view(), name='logout'),
    path('profile/', UserProfileView.as_view(), name='my_profile'),
    path('profile/<pk>/', ProfileByPkView.as_view(), name='profile')
    
]
