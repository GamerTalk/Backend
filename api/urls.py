from django.urls import path
from . import views

urlpatterns = [
    path('', views.hello),
    path('test/', views.testhello),
    path('new-user/', views.NewUser),
]
