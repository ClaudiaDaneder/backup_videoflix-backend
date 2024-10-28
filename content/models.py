from datetime import datetime
from django.db import models
from multiselectfield import MultiSelectField

CATEGORIES = (
    ('music', 'Music'),
    ('nature', 'Nature'),
    ('animals', 'Animals'),
    ('city', 'City Life')
)

class Video(models.Model):
    video_file = models.FileField(upload_to='videos_uploaded/original')
    video_360p_path = models.CharField(max_length=255, blank=True)
    date_uploaded = models.DateField(default=datetime.now)
    title = models.CharField(max_length=100)
    description = models.CharField(max_length=2000)
    categories = MultiSelectField(choices=CATEGORIES, max_length=200)
    thumbnail_path = models.CharField(max_length=255, blank=True)

    def __str__(self):
        return self.title
