import boto3
from django.http import HttpResponse
from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response
from config.configConstants import (AWSConstants, NotificationConstants, DeviceType)
import json
from botocore.exceptions import ClientError


class SNSNotification():

    def send_push_notification(title, body, endpoint, deviceType, data):
        try:

            # Create an SNS client
            client = boto3.client('sns',
            # aws_access_key_id= AWSConstants.AWS_ACCESS_KEY_ID,
            # aws_secret_access_key= AWSConstants.AWS_SECRET_ACCESS_KEY,
            # region_name= AWSConstants.AWS_REGION
            aws_access_key_id= "",
            aws_secret_access_key= "",
            region_name= ""
            )

            if deviceType == 'ANDROID':
                #dataDict = {'notification':{'title':title,'body':body}, 'data': data}
                dataDict = {'data':{'title':title,'body':body,'data': data}}
                print('.......................',dataDict)
                dataString = json.dumps(dataDict,ensure_ascii=False)
                message = {'default':'default message','GCM':dataString}
                messageJSON = json.dumps(message,ensure_ascii=False)
                
            if deviceType == 'IOS':
                apnsDict = {'aps':{'alert':{'title':title,'body':body}, 'data': data}}
                print('.......................',apnsDict)
                apnsString = json.dumps(apnsDict,ensure_ascii=False)
                #message = {'default':'default message','APNS_SANDBOX':apnsString}
                message = {'SANDBOX':apnsString}
                messageJSON = json.dumps(message,ensure_ascii=False)

  
            # Publish a simple message to the specified SNS topic
            response = client.publish(
            TargetArn=endpoint,
            Message= messageJSON,
            MessageStructure= 'json'
            )
            print(response)

        except Exception as e:
            print(str(e))
            return Response(str(e), status=status.HTTP_500_INTERNAL_SERVER_ERROR)


    def send_sms(phone, message):
        try:
            print(phone)
            # Create an SNS client
            client = boto3.client('sns',
            aws_access_key_id= AWSConstants.AWS_ACCESS_KEY_ID,
            aws_secret_access_key= AWSConstants.AWS_SECRET_ACCESS_KEY,
            region_name= AWSConstants.AWS_REGION)

            # Send your sms message.
            response = client.publish(
                PhoneNumber=str(phone),
                Message=message
            )
            print(response)

        except Exception as e:
            print(str(e))
            return Response(str(e), status=status.HTTP_500_INTERNAL_SERVER_ERROR)


    def send_email(senderEmail, recipientEmail, subject, message):
        # Replace sender@example.com with your "From" address.
        # This address must be verified with Amazon SES.
        SENDER = senderEmail

        # Replace recipient@example.com with a "To" address. If your account 
        # is still in the sandbox, this address must be verified.
        RECIPIENT = recipientEmail

        # The subject line of the email.
        SUBJECT = subject

        # The body of the email for recipients whose email clients don't support HTML
        # content.
        BODY_TEXT = message

        # The body of the email for recipients whose email clients can display HTML
        # content.
        BODY_HTML = f'<table cellpadding="0" cellspacing="0" style="width: 100%;float:left"><tr><td align="center"><table cellpadding="0" cellspacing="0" style="max-width: 650px;width: 100%;background:#eaeaea;"><tr><td style="font-size:18px; background:#307abc; color:#fff;padding:10px 0"><p style="text-align:center;display: block;margin: 0 auto;">Test</p></td> </tr><tr><td><table style="width:100%;background:#eaeaea;padding: 20px"><tr><td style="background: #fff;padding: 20px;"><h3 style="font-size:18px;margin-bottom:10px;margin-top: 0;text-align: center">{SUBJECT}</h3>{BODY_TEXT}</td></tr></table></td></tr><tr><td></tr></table>'

        # The character encoding for the email.
        CHARSET = "UTF-8"

        # Create a new SES resource and specify a region.
        client = boto3.client('ses',
            aws_access_key_id= AWSConstants.AWS_ACCESS_KEY_ID,
            aws_secret_access_key= AWSConstants.AWS_SECRET_ACCESS_KEY,
            region_name= AWSConstants.AWS_REGION)

        # Try to send the email.
        try:
            #Provide the contents of the email.
            response = client.send_email(
                Destination={
                    'ToAddresses': [
                        RECIPIENT,
                    ],
                },
                Message={
                    'Body': {
                        'Html': {
                            'Charset': CHARSET,
                            'Data': BODY_HTML,
                        },
                        'Text': {
                            'Charset': CHARSET,
                            'Data': BODY_TEXT,
                        },
                    },
                    'Subject': {
                        'Charset': CHARSET,
                        'Data': SUBJECT,
                    },
                },
                Source=SENDER,
            )


        except ClientError as e:
            return Response({'error':str(e.response['Error']['Message'])}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)


    def create_platform_endpoint(deviceToken, deviceType):
        
        # Create an SNS client
        client = boto3.client('sns',
        # aws_access_key_id= AWSConstants.AWS_ACCESS_KEY_ID,
        # aws_secret_access_key= AWSConstants.AWS_SECRET_ACCESS_KEY,
        # region_name= AWSConstants.AWS_REGION
        aws_access_key_id= "",
        aws_secret_access_key= "",
        region_name= ""
        )

        # For android
        if deviceType == DeviceType.ANDROID:
            response = client.create_platform_endpoint(
            PlatformApplicationArn=NotificationConstants.ANDROID_APPLICATION_ARN,
            Token=deviceToken  
            )

        # For iOS
        if deviceType == DeviceType.IOS:
            response = client.create_platform_endpoint(
            PlatformApplicationArn=NotificationConstants.IOS_APPLICATION_ARN,
            Token=deviceToken
            )
        
        endpointARN = response['EndpointArn']
        return endpointARN
        
        
