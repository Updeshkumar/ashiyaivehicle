from rest_framework import serializers
from user.models import Requirement


class ProfileSerializer(serializers.ModelSerializer):
    class Meta:
        model = Requirement
        fields = ['Id', 'title', 'description', 'requirement_image']