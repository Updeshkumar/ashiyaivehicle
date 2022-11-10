from django.shortcuts import render
from rest_framework.decorators import api_view
from cerberus import errors, Validator
from utility.requestErrorFormate import requestErrorMessagesFormate
from rest_framework import status
from rest_framework.response import Response
from utility.sqlQueryBuilder import SqlQueryBuilder
from utility.passwordHashing import PasswordHashing
from django.views.decorators.csrf import csrf_exempt
from user.models import (User,Device)
from config.messages import Messages
from django.db import transaction
from utility.jwtTokenHelper import JwtTokenHelper
from utility.authMiddleware import isAuthenticate
from utility.SNSNotifications import SNSNotification
from datetime import datetime, timedelta
from utility.customValidations import CustomValidator
from random import randint
from config.configConstants import (UserType, DeviceType, OTPActionType, VerificationLink, JWTConstants, AdminConstants)
#from utility.aesEncryption import AESEncryption
from django.db.models import Q
import pytz,uuid
from django.http import HttpResponse

# Create your views here.

# generate access and refresh token 
def access_refresh_token(tokenData):

    data = JwtTokenHelper().CreateToken(tokenData)
   
    data = {
        "accessToken": data['accessToken'],
        "refreshToken": data['refreshToken']
    }
    return data


# This method is use for login
@csrf_exempt
@api_view(['POST'])
def login(request):
    try:
        schema = {
            "password": {'type': 'string', 'required': True, 'empty': False},
            "username": {'type': 'string', 'required': True, 'empty': False},
            "deviceType": {'type': 'string', 'required': True, 'empty': False, 'allowed': [DeviceType.WEB]}, 
        }
        v = Validator()
        if not v.validate(request.data, schema):
            return Response(requestErrorMessagesFormate(v.errors), status=status.HTTP_400_BAD_REQUEST)

    except Exception as e:
        return Response({'error':str(e)}, status=status.HTTP_400_BAD_REQUEST)
    try:
        passwordHashing = PasswordHashing()        

        # if user enters email
        if User.objects.filter(username=request.data['username'], user_type=UserType.ADMIN).exists():
            
            userInformation = User.objects.filter(username=request.data['username'], user_type=UserType.ADMIN).values()
            userId = userInformation[0]['user_id']
            userPassword = userInformation[0]['password']
            userType = userInformation[0]['user_type']
            firstName = userInformation[0]['first_name']
            userName = userInformation[0]['username']
            profilePic = userInformation[0]['profile_pic']
            countryCode = userInformation[0]['country_code']
            mobileNo = userInformation[0]['mobile_number']
             
        else:
            return Response({'error':Messages.USERNAME_OR_PASSWORD_PHONE_INCORRECT}, status=status.HTTP_200_OK)

        # match the password, if same then continue
        
        #try:
         #   password = AESEncryption().decrypt(request.data['password'])
        #except Exception as e:
         #   return Response({'error':Messages.USERNAME_OR_PASSWORD_PHONE_INCORRECT}, status=status.HTTP_200_OK)
        if passwordHashing.matchHashedPassword(userPassword,request.data['password']):
            # generate token 
            tokenInput = {
            'userId': userId,
            'userType': userType,
            'firstName': firstName,
            'username': userName,
            'profilePic': profilePic if profilePic else '' ,
            'countryCode': countryCode,
            'mobileNo': mobileNo
            }
            tokenData = access_refresh_token(tokenInput)

            with transaction.atomic():
                if Device.objects.filter(created_by=userId).exists():
                    Device.objects.filter(created_by=userId).update(                    
                        refresh_token=tokenData['refreshToken'],
                        device_type = request.data['deviceType'],
                        is_active=1)
                else: 
            # insert data in device table
                    Device.objects.create(
                        refresh_token=tokenData['refreshToken'],
                        device_type = request.data['deviceType'],
                        created_by=User.objects.get(user_id=userId),
                        is_active=1
                    )
                
                data = {
                    "accessToken": tokenData['accessToken'],
                    "refreshToken": tokenData['refreshToken']
                }
                
                return Response(data, status=status.HTTP_200_OK)
        return Response({'error':Messages.USERNAME_OR_PASSWORD_PHONE_INCORRECT}, status=status.HTTP_200_OK)
        
    except Exception as e:
        return Response({'error':e}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)

# This method is use to send otp on mobile
@api_view(['POST'])
def send_otp_mobile(request):
    try:
        schema = {
            "countryCode": {'type': 'integer', 'required': True, 'nullable': False},
            "mobileNo": {'type': 'string', 'required': True, 'empty': False},
            "actionType": {'type': 'string', 'required': True, 'empty': False, 'allowed': [OTPActionType.REGISTRATION, OTPActionType.FORGOT_PASSWORD]},
        }
        v = Validator()
        if not v.validate(request.data, schema):
            return Response(requestErrorMessagesFormate(v.errors), status=status.HTTP_400_BAD_REQUEST)
    except Exception as e:
        return Response({'error':str(e)}, status=status.HTTP_400_BAD_REQUEST)
    try:       
        mobileNo = request.data['mobileNo']
        countryCode = request.data['countryCode']
        actionType = request.data['actionType']
        
        if OTPActionType.REGISTRATION == actionType:
            # check if mobile number exists
            if User.objects.filter(mobile_number=mobileNo,country_code=countryCode).exists():
                return Response({'error':Messages.MOBILE_EXISTS}, status=status.HTTP_200_OK) 
        
        if OTPActionType.FORGOT_PASSWORD == actionType:
            # check if mobile number exists
            if not User.objects.filter(mobile_number=mobileNo,country_code=countryCode).exists():
                return Response({'error':Messages.MOBILE_DOES_NOT_EXISTS}, status=status.HTTP_200_OK)   
                            
        # Generate random otp
        otp = str(randint(1000, 9999))
        otpToSave = otp
        # Send SMS
        countryCode = str(countryCode)
        message = str(otp)+" is your verification code for Ascend App." 
        SNSNotification.send_sms(countryCode+mobileNo, message)
        otp = {'otp':AESEncryption().encrypt(otp)}
        User.objects.filter(mobile_number=mobileNo, country_code = countryCode).update(                    
                    otp=AESEncryption().encrypt(otpToSave))
        return Response({'data':otp}, status=status.HTTP_200_OK)  
    except Exception as e:
        print('send_otp_mobile',str(e))
        return Response({'error': Messages.SOMETHING_WENT_WRONG}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)


# This method is use to get the access token from refresh token
@api_view(['POST'])
def access_token(request):
    try:
        schema = {
            "refreshToken": {'type': 'string', 'required': True, 'empty': False},
            "userId": {'type': 'integer', 'required': True, 'nullable': False},
        }
        v = Validator()
        if not v.validate(request.data, schema):
            return Response(requestErrorMessagesFormate(v.errors), status=status.HTTP_400_BAD_REQUEST)
    except Exception as e:
        return Response({'error':str(e)}, status=status.HTTP_400_BAD_REQUEST)
    try:
        userId = request.data["userId"]
        if not User.objects.filter(user_id=userId).exists():
            return Response({'message':Messages.USER_NOT_EXISTS}, status=status.HTTP_401_UNAUTHORIZED)
        refreshToken = request.data['refreshToken']  # get token from header
        payload = JwtTokenHelper().getJWTPayload(refreshToken)  # get the payload from token
        if payload:
            expirationTime = payload["exp"]
            timestamp = datetime.fromtimestamp(expirationTime)
            userToken = Device.objects.filter(created_by = userId).order_by('-created_at')[0:1].values()
            utc=pytz.UTC
            user_expire_datetime = timestamp + timedelta(minutes=10)

            # Current datetime
            current_datetime = datetime.now()

            # replace the timezone in both time
            expiredOn = user_expire_datetime.replace(tzinfo=utc)
            checkedOn = current_datetime.replace(tzinfo=utc)

            if userToken:
                if (userToken[0]['refresh_token'] == refreshToken):
                    if  checkedOn  > expiredOn:  # token expired
                        return Response({'error': Messages.REFRESH_TOKEN_EXPIRED}, status=status.HTTP_401_UNAUTHORIZED)
                    else:                        
                        # Fetch User Info
                        userInfo = User.objects.filter(user_id=userId).values()
                        
                        # get the access token
                        accessToken = JwtTokenHelper().JWTAccessToken({
                            'userId': userInfo[0]['user_id'],
                            'userType': userInfo[0]['user_type'],
                            'firstName': userInfo[0]['first_name'],
                            'lastName': userInfo[0]['last_name'],
                            'username': userInfo[0]['username'],
                            'profilePic': userInfo[0]['profile_pic'] if userInfo[0]['profile_pic'] else '' ,
                            'countryCode': userInfo[0]['country_code'],
                            'mobileNo': userInfo[0]['mobile_number']
                        })
                        
                        result = {
                            "accessToken": accessToken
                        }
                        return Response(result, status=status.HTTP_200_OK)
                else:
                    return Response({'error': Messages.INVALID_REFRESH_TOKEN}, status=status.HTTP_401_UNAUTHORIZED)
            else:
                return Response({'error': Messages.INVALID_REFRESH_TOKEN}, status=status.HTTP_401_UNAUTHORIZED)
        else:
            return Response({'error': Messages.REFRESH_TOKEN_EXPIRED}, status=status.HTTP_401_UNAUTHORIZED)

    except Exception as e:
        return Response({'error': Messages.SOMETHING_WENT_WRONG}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)
    
# This method is used to send the verification link in forget password
@api_view(['POST'])
def forgot_password(request):
    try:
        schema = {
            "email": {'isEmail': True, 'type': 'string', 'required': True, 'empty':False}
        }
        v = CustomValidator()
        # Validate the request
        if not v.validate(request.data, schema):
            return Response(requestErrorMessagesFormate(v.errors), status=status.HTTP_400_BAD_REQUEST)
    except Exception as e:
        return Response({'error':str(e)}, status=status.HTTP_400_BAD_REQUEST)
    try:
        # Get data from request
        email = request.data['email'].lower()
        print(email)
        token = uuid.uuid4().hex  # generate a random hex key
        print(token)

        #If account is blocked by admin
        if not User.objects.filter(username=email).exists():
            return Response({'error':Messages.USER_NOT_EXISTS}, status=status.HTTP_200_OK)

        # Fetch User info
        userInfo = User.objects.filter(username=email).values()  # check email exists or not
        if userInfo:
            userId = userInfo[0]['user_id']
            print(userId)
            User.objects.filter(user_id=userId).update(
                    verification_key= token)  # update the verification key

            # generate a token along with KEY
            token = JwtTokenHelper().forgotPasswordToken(
                {
                    'email': email, 
                    'userId': userId, 
                    'key': token,
                    'exp': datetime.utcnow() + timedelta(seconds=JWTConstants.FOROGOT_EXP_DELTA_SECONDS)
                })
            print(token)
            
            # Generate a verification link which will send to user email id
            link = VerificationLink().FORGOT_PASSWORD_LINK+'set-password/' + token
            # subject and body for email
            subject = "Password Reset Link"
            body = '<h3>'+"Hello"+" "+userInfo[0]['first_name']+","+"</h3><p>Hopefully you have requested to reset the password for your Ascend account. If you did not perform this request, You can safely ignore this email. Otherwise, Click the link below to complete the process.</p><br><br>" + \
                '<a href='+link+' target="_blank" style="display:inline-block;background:#2c8ae3; padding:7px 10px;color:#fff; text-decoration:none; display:inline-block; text-align:center; margin:10px auto 0; border-radius:4px">Click here</a>'+'<p>Regards,</p><p>Ascend Team</p>'
            
            #send mail
            SNSNotification.send_email(AdminConstants.ADMIN_EMAIL, email, subject, body)
            
            return Response({'data': Messages.FORGOT_PASSWORD_LINK_SEND}, status=status.HTTP_200_OK)
        else:
            return Response({'error': Messages.USER_NOT_EXISTS}, status=status.HTTP_200_OK)

    except Exception as e:
        print("admin_forgot_password", str(e))
        return Response({'error': Messages.SOMETHING_WENT_WRONG}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)

# This method is used to verify password reset token
@api_view(['POST'])
def verify_token(request):
    try:
        schema = {
            "token": {'type': 'string', 'required': True, 'empty': False}
        }
        v = Validator()

        # Validate the request
        if not v.validate(request.data, schema):
            return Response(requestErrorMessagesFormate(v.errors), status=status.HTTP_400_BAD_REQUEST)

    except Exception as e:
        return Response({'error':str(e)}, status=status.HTTP_400_BAD_REQUEST)

    try:
        token = request.data["token"]
        payload = JwtTokenHelper().getJWTPayload(token)
        
        if payload:
            user_id = payload['userId']
            userInfo = User.objects.filter(user_id=user_id, verification_key=payload['key']).values()
            if userInfo:
                return Response({'message': Messages.TOKEN_VERIFIED}, status=status.HTTP_200_OK)
            else:
                return Response({'error': Messages.INVALID_TOKEN}, status=status.HTTP_200_OK)
        else:
            return Response({'error': Messages.INVALID_TOKEN}, status=status.HTTP_200_OK)

    except Exception as e:
        print("admin_verify_token", str(e))
        return Response({'error': Messages.SOMETHING_WENT_WRONG}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)
    
# This method is admin used to reset password
@api_view(['PUT'])
def reset_password(request):
    try:
        schema = {
            "token": {'type': 'string', 'required': True, 'empty': False},
            "password": {'type': 'string', 'required': True, 'empty': False}
        }
        v = Validator()

        # Validate the request
        if not v.validate(request.data, schema):
            return Response(requestErrorMessagesFormate(v.errors), status=status.HTTP_400_BAD_REQUEST)

    except Exception as e:
        return Response({'error':str(e)}, status=status.HTTP_400_BAD_REQUEST)

    try:
        passwordHashing = PasswordHashing()
        token = request.data["token"]
        payload = JwtTokenHelper().getJWTPayload(token)
        
        if payload: 

            # decrypt password
            try:
                password = AESEncryption().decrypt(request.data['password'])
            except Exception as e:
                return Response({'error':Messages.INVALID_PASSWORD}, status=status.HTTP_400_BAD_REQUEST)
            

            userId = payload['userId']
            userInfo = User.objects.filter(user_id=userId, verification_key=payload['key']).values()
            if userInfo:
                
                # password hashing
                hashPassword = PasswordHashing().getHashedPassword(password)
                
                # update the verification key as well as password
                User.objects.filter(user_id=userId).update(verification_key=None, password=hashPassword)
                return Response({'message': Messages.PASSWORD_UPDATE}, status=status.HTTP_200_OK)
            else:
                return Response({'error': Messages.LINK_EXPIRED}, status=status.HTTP_200_OK)
        else:
            return Response({'error': Messages.LINK_EXPIRED}, status=status.HTTP_200_OK)

    except Exception as e:
        print("admin_reset_password", str(e))
        return Response({'error': Messages.SOMETHING_WENT_WRONG}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)

