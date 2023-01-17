from django.urls import path
from rest_framework import routers
from . import views
from . import admin_views

router = routers.DefaultRouter()

urlpatterns = [
    path('login/auth', admin_views.login),
    #path('users', views.get_all_users),    
    #path('profile/<int:userId>', views.get_user_profile_detail),
    #path('block-user', views.block_user),
    #path('delete-user', views.delete_user),
    #path('block-users', views.get_block_users),
    #path('unblock-user', views.unblock_user),
    #path('get-admin-menus', views.get_admin_menus),
    #path('create-subadmin', views.create_subadmin),
    #path('edit-subadmin', views.edit_subadmin),
   ## path('get-subadmin-list', views.get_subadmin_list),
    #path('save-cpm-details', views.save_cpm_details),
    #path('content-economy', views.get_content_economy),
    # path('save-cofigurations', views.save_cofigurations),
    # path('get-configuration-details', views.get_configuration_details),
    # path('user-transaction-details', views.admin_get_user_transaction),
    # path("get-creator-users", views.get_creator_users),
    # path("get-bank-details", views.get_bank_details),
    # path("save-master-data", views.save_master_data),
]

urlpatterns += router.urls
