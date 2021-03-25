from django.urls import path
from generator import views

urlpatterns = [
    path('', views.home, name='home'),
    path('pwdgen', views.pwdgen, name="pwdgen"),
]