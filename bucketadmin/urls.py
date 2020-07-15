from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('',views.FresherRegister,name="FresherRigister"),
    path('FresherRigister',views.FresherRegister,name="FresherRegister"),
    path('CompanyRegister',views.CompanyRegister,name="CompanyRegister"),
    path('Posting',views.Posting,name='Posting'),
    path('<int:User_id>/Companyprofile_data/',views.Companyprofile_data,name='Companyprofile_data'),
    path('Json_Data',views.Json_Data.as_view(),name='Json_Data'),
    path('Login',views.Login,name='Login'),
    path('check_out',views.Logout,name='Logout'),
]