import jwt
from rest_framework import status
from rest_framework.response import Response
from config.configConstants import JWTConstants, AnonymousReqSecret


# This function is used to authenticate after login
def isAuthenticate(function):
    def wrap(request, *args, **kwargs):
        try:
            if request.META.get('HTTP_AUTHORIZATION') and request.META.get('HTTP_AUTHORIZATION') != 'invalidtoken':
                token = request.META.get('HTTP_AUTHORIZATION')
                # validating access token
                try:
                    # Decode payload
                    payload = jwt.decode(token, JWTConstants.TOKEN_SECRET,
                                         algorithms=[JWTConstants.JWT_ALGORITHM])
                    request.userId = payload["userId"]
                    request.userType = payload["userType"]
                    # Token is valid pass the request
                    return function(request, *args, **kwargs)
                except jwt.exceptions.DecodeError:
                    return Response({'message': "Invalid Access Token"},
                                    content_type="application/json", status=status.HTTP_500_INTERNAL_SERVER_ERROR)
                except jwt.exceptions.InvalidSignatureError:
                    return Response({'message': "Invalid Access Token"},
                                    content_type="application/json", status=status.HTTP_500_INTERNAL_SERVER_ERROR)
                except jwt.exceptions.ExpiredSignatureError:
                    return Response({'message': "Access Token expired"},
                                    content_type="application/json", status=status.HTTP_401_UNAUTHORIZED)
                except jwt.exceptions.InvalidTokenError:
                    return Response({'message': "Invalid Access Token"},
                                    content_type="application/json", status=status.HTTP_500_INTERNAL_SERVER_ERROR)
            else:
                return Response({'message': 'Authentication credentials were not provided.'},
                                content_type="application/json", status=status.HTTP_500_INTERNAL_SERVER_ERROR)
        except BaseException as e:
            return Response({'message': str(e)}, content_type="application/json", status=status.HTTP_400_BAD_REQUEST)

    return wrap
