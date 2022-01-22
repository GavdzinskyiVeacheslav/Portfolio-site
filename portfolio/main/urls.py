from django.urls import path
from. import views
from .views import *

urlpatterns = [
    path('', views.index, name='home'),
    path('about', views.about, name='about'),
    path('register/', RegisterUser.as_view(), name='register'),
    path('login/', LoginUser.as_view(), name='login'),
    path('logout/', logout_user, name='logout'),

]
