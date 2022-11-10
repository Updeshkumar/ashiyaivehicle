import requests
import json
class FirebaseNotification():
    def sendNotification(title, topicName, bodyData):
        url = "https://fcm.googleapis.com/fcm/send"
        headers = {"Content-Type": "application/json; charset=utf-8", "Authorization":"key=AAAAOcEssFo:APA91bEmB0nClnCs_oXO44AWaNu7Vbomw4Z_zlxdEGJKIvTu72PtduZqA-nLvbTNMQaP_bLHpddujX7WRPIFc0H5oYZSaUSYShAkOwXPqwjeHXHgD5BsLulPhi4-icZLSUS585UY2qf2"}
        data = {
        	"to" : "/topics/"+str(topicName),
        	"notification" : {
        		"body" : bodyData,
        		"title": title
        		}
        	}
        response = requests.post(url, headers=headers, json=data)
        return response