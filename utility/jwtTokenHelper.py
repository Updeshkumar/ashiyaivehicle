import jwt
from datetime import datetime
from datetime import timedelta
from config.configConstants import JWTConstants
import secrets 
import string 

class JwtTokenHelper:

    # Decode the jwt token and get the payload
    def getJWTPayload(self, token):
        try:
            payload = jwt.decode(token, JWTConstants.TOKEN_SECRET,
                                 algorithms=[JWTConstants.JWT_ALGORITHM])
            if payload:
                return payload
            else:
                return None
        except Exception as e:
            return False

    # create the forget password token
    def forgotPasswordToken(self, obj):
        try:
            payload = jwt.encode(obj, JWTConstants.TOKEN_SECRET, algorithm=JWTConstants.JWT_ALGORITHM)
            if payload:
                return payload
            else:
                return None
        except Exception as e:
            return False


    # JWT access token generation
    def JWTAccessToken(self, user):
        try:

            user['exp']=datetime.utcnow() + timedelta(seconds=JWTConstants.JWT_EXP_DELTA_SECONDS)
            payload=user
            accessToken = jwt.encode(payload, JWTConstants.TOKEN_SECRET, algorithm=JWTConstants.JWT_ALGORITHM)
            
            return accessToken
        except Exception as e:
            return False


    # JWT refresh token generation
    def JWTRefreshToken(self, user):
        try:
            user['exp']=datetime.utcnow() + timedelta(seconds=JWTConstants.JWT_REF_EXP_DELTA_SECONDS)
            payload=user
            refreshToken = jwt.encode(payload, JWTConstants.REFRESH_TOKEN_SECRET, algorithm=JWTConstants.JWT_ALGORITHM)
            return refreshToken
        except Exception as e:
            return False

    # Append random string to access token 
    def CreateToken(self, user):
        try:
            # generate access token
            accessToken = self.JWTAccessToken(user) 
            # generate refresh token
            refreshToken = self.JWTRefreshToken(user)  
            
            data = {
                "accessToken": accessToken,
                "refreshToken": refreshToken
            }
            return data
        except Exception as e:
            return False
