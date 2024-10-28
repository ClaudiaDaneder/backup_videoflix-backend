from django.contrib import admin
from import_export import resources
from import_export.admin import ImportExportModelAdmin
from .models import Video

class VideoResource(resources.ModelResource):
    class Meta:
        model = Video

class VideoAdmin(ImportExportModelAdmin):
    resource_classes = [VideoResource]
    # exclude = ('thumbnail_path', 'date_uploaded', 'video_360p_path')

admin.site.register(Video, VideoAdmin)
