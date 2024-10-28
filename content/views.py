from django import views
from django.conf import settings
from rest_framework import viewsets
from rest_framework.response import Response
from rest_framework.views import APIView
from content.models import CATEGORIES, Video
from content.serializers import VideoSerializer
from rest_framework.authentication import TokenAuthentication
from rest_framework.permissions import IsAuthenticated
from django.core.cache.backends.base import DEFAULT_TIMEOUT
from django.core.cache import cache

CACHE_TTL = getattr(settings, 'CACHETTL', DEFAULT_TIMEOUT)

class VideoViewSet(viewsets.ViewSet):
    # authentication_classes = [TokenAuthentication]
    # permission_classes = [IsAuthenticated]
    """
    A simple ViewSet for listing or retrieving users.
    """
    def list(self, request):
        cache_key = 'video_list'
        cached_data = cache.get(cache_key)
        if cached_data:
            return Response(cached_data)

        queryset = Video.objects.all()
        serializer = VideoSerializer(queryset, many=True)
        response_data = serializer.data
        cache.set(cache_key, response_data, CACHE_TTL)
        return Response(response_data)


class CategoriesView(APIView):
    authentication_classes = [TokenAuthentication]
    permission_classes = [IsAuthenticated]

    def get(self, request):
        categories = [
            {
                'value': key,
                'name': name
            } for key, name in CATEGORIES
        ]
        return Response(categories)