from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('doc-login/', views.signin, name='sigin'),
    path('doc-profile/', views.signin, name="test")
]