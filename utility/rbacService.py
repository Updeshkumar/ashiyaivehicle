""" 
 Service for role based access control.
 Provides simple method for checking permissions.
"""

from django.http import HttpResponse
from functools import wraps
from rest_framework import status
from user_auth.models import (User,Device)
from user.models import (Profile)
from rest_framework.response import Response
from roles.models import (RoleAccessModel, RoleModel)

"""
Check the existence of the permissions or attributes on the user of the given rbacArray
returns True, if the user has any combination of permissions, False otherwise
"""
def rbacService(function):
    def wrap(request, *args, **kwargs):
        try:
            permission = request.permissions
            print(permission)
            # Fetch User Info
            userInfo = User.objects.filter(user_id=request.userId).values()
            userPermission = []
            print(userInfo[0]['role_id'])
            if userInfo[0]['role_id'] != None:
                print("hiiiiii how are you")
                # Fetch User Role Permissions 
                userRoleInfo = RoleAccessModel.objects.filter(role_id=RoleModel.objects.get(role_id = userInfo[0]['role_id'])).values() 
                for obj in userRoleInfo:
                    userPermission.append(
                        obj['menu_id_id']
                    )

            if userPermission == permission:
                return function(request, *args, **kwargs)
            else:
                return Response({'message': "You don't have permission to access!"},
                                content_type="application/json", status=status.HTTP_401_UNAUTHORIZED)
                
        except Exception as e:
            print('rbacService', str(e))
            return Response({'message': str(e)}, content_type="application/json", status=status.HTTP_400_BAD_REQUEST)
    return wrap


def process_exception(self, request, exception):
    print('rbacServiceException', str(exception.message))
    print(exception.__class__.__name__)
    print(exception.message)
    return None
