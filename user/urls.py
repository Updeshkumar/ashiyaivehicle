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
    path('postmasterdata', views.save_master_data),
    path('hvbesicdetails', views.hvregistration), 
    path('hvaddress', views.hvaddress, name="hvaddress"),
    path('reqheavyvehicle', views.requesthvregistration),
    path('doregistrations', views.doregistration),
    path('reqdriveroperator', views.requestdoperator),
    path('subcregistration', views.subcregistration),
    path('reqsubcontractor', views.reqsubcon),
    path('lacoregistration', views.lacoregistration),
    path('reqlacontractor', views.requestlacontractor),
    path('logout', views.logout),
    path('filter_data', views.filter_data),
    path('listrequirement/', views.ProfileView.as_view(), name="list" ),
    path('images/', views.ImageView.as_view(), name="images"),
    path('normaluser', views.normaluserregistration, name="normaluser"),
    path("sp", views.saverecordemp),

]

urlpatterns += router.urls
