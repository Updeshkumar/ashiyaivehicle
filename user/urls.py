from django.urls import path
from rest_framework import routers
from . import views

router = routers.DefaultRouter()

urlpatterns = [

    path('uploadFile', views.uploadFile),
    path('otp-verify', views.verify_mobile_otp),
    path('send-otp', views.send_otp_mobile),
    path('access-token', views.access_token),
    path('user/<int:userId>', views.get_user_profile),
    path('user', views.update_user_profile),
    path('master_data', views.get_master_data),
    path('hvbesicdetails', views.hvregistration), 
    path('reqheavyvehicle', views.reqeusthvregistration),
    path('doregistrations', views.doregistration),
    path('subcregistration', views.subcregistration),
    path('lacoregistration', views.lacoregistration),
    path('logout', views.logout),
    path('filter_data', views.filter_data),
    path('allrequirement', views.allrequirement),

]

urlpatterns += router.urls
