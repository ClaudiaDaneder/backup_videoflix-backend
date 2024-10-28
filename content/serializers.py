from rest_framework import serializers
from content.models import Video
from rest_framework import fields, serializers
from content.models import CATEGORIES


class VideoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Video
        fields = '__all__'
