from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('doc-login/', views.signin, name='signin'),
    path('doc-profile/', views.retrive_p_data, name="doc-profile")
]