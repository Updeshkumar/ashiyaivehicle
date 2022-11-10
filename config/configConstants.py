from dotenv import dotenv_values
config = dotenv_values(".env")

class JWTConstants():
    JWT_ALGORITHM = config.get('JWT_ALGORITHM')
    JWT_EXP_DELTA_SECONDS = int(config.get('JWT_EXP_DELTA_SECONDS'))  # valid upto 5 hours
    JWT_EXP_DELTA_DAYS = int(config.get('JWT_EXP_DELTA_DAYS'))
    JWT_REF_EXP_DELTA_SECONDS = int(config.get('JWT_REF_EXP_DELTA_SECONDS'))  # valid upto 30 days
    TOKEN_SECRET = config.get('JWT_TOKEN_SECRET')
    REFRESH_TOKEN_SECRET = config.get('JWT_REFRESH_TOKEN_SECRET')
    REFRESH_TOKEN_SALT = config.get('JWT_REFRESH_TOKEN_SALT')
    FOROGOT_EXP_DELTA_SECONDS = int(config.get('JWT_FOROGOT_EXP_DELTA_SECONDS'))
class passwordSalt():
    SALT = config.get('PASSWORD_SALT')  # uuid.uuid4().hex
class AnonymousReqSecret:
    CLIENT_SECRET = config.get('ANONYMOUS_CLIENT_SECRET')
class AWSConstants():
    AWS_ACCESS_KEY_ID = config.get('AWS_ACCESS_KEY_ID')
    AWS_SECRET_ACCESS_KEY = config.get('AWS_SECRET_ACCESS_KEY')
    AWS_REGION = config.get('AWS_REGION')
    S3_BUCKET = config.get('S3_BUCKET')
class NotificationConstants():
    ANDROID_APPLICATION_ARN = config.get('ANDROID_APPLICATION_ARN')
    IOS_APPLICATION_ARN = config.get('IOS_APPLICATION_ARN')

class UserType():
    ADMIN = config.get('USER_TYPE_ADMIN')
    USER = config.get('USER_TYPE_USER')
    
class DeviceType():
    ANDROID = config.get('DEVICE_TYPE_ANDROID')
    IOS = config.get('DEVICE_TYPE_IOS')
    WEB = config.get('DEVICE_TYPE_WEB')

class OTPActionType():
    REGISTRATION = config.get('OTP_ACTION_TYPE_REGISTRATION')
    FORGOT_PASSWORD = config.get('OTP_ACTION_TYPE_FORGOT_PASSWORD')

class AESEncryptionKeys():
    AES_SECRET_KEY = bytes(config.get('AES_SECRET_KEY'), 'utf-8')
    AES_SECRET_IVKEY = bytes(config.get('AES_SECRET_IVKEY'), 'utf-8')
    AES_SIZE = config.get('AES_SIZE')

class VerificationLink():
    FORGOT_PASSWORD_LINK = config.get('FORGOT_PASSWORD_LINK')

class AdminConstants():
    ADMIN_EMAIL = config.get('ADMIN_EMAIL')
    
class HumanticKey():
    API_KEY = config.get('HUMANTIC_API_KEY')

class ConnectionType():
    FACEBOOK = config.get('FACEBOOK')
    TWITTER = config.get('TWITTER')
    
class MediaType():
    VIDEO = config.get('MEDIA_VIDEO')
    IMAGE = config.get('MEDIA_IMAGE')
    TEXT = config.get('MEDIA_TEXT')
class ActionType():
    ADD = config.get('ACTION_ADD')
    REMOVE = config.get('ACTION_REMOVE')
class ReasonType():
    USER = config.get('REASION_USER')
    POST = config.get('REASION_POST')
    COMMENT = config.get('REASION_COMMENT')
    BELOW_POST_RATING = config.get('REASION_BELOW_POST_RATING')
class FollowType():
    FOLLOWERS = 'FOLLOWERS'
    FOLLOWING = 'FOLLOWING'    
class UserBlockType():
    VISIBLE = 'VISIBLE'
    INVISIBLE = 'INVISIBLE'


    