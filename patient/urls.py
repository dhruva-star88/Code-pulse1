from django.urls import path
from . import views

urlpatterns = [
    path('pat-id-page/', views.pat_id_page, name='pat-id-page'),
    path('pat-id-page/pat-hosp-record/', views.pat_hosp_record, name="pat_hosp_record"),
]