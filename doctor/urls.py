from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('doc-login/', views.signin, name='signin'),
    path('doc-login/doc-profile/', views.retrive_p_data, name="doc_profile"),
    path('doc-login/doc-profile/pat-details/', views.pat_report, name='pat_report'),
    path('doc-login/doc-profile/pat-details/pat-report/', views.doc_to_pat_report, name='doc_to_pat_report'),
    path('doc-login/doc-profile/pat-details/pat-prev-rec/', views.pat_prev_rec, name='pat_prev_record'),
    path('doc-login/doc-profile/pat-details/pat-prev-rec/edit-record/', views.edit_record, name='edit_record'),
]

# path('doc-profile/', views.retrive_p_data, name="doc-profile")