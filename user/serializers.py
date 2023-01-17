from rest_framework import serializers
from user.models import Requirement, VedioUplaod

class VedioSerailzer(serializers.ModelSerializer):
    class Meta:
        model = VedioUplaod
        fields = ['Id', 'image_uplaod', 'vediourl']



class ProfileSerializer(serializers.ModelSerializer):
    class Meta:
        model = Requirement
        fields = ['Id', 'title', 'description', 'requirement_image']