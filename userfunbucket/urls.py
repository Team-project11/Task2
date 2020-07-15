from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('<int:User_id>/ProfileData/',views.ProfileData,name='ProfileData'),
]