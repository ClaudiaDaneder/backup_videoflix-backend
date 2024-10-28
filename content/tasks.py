import os
import subprocess
from content.models import Video
from django_rq import job


@job
def convert360p(source, video_id):
    base, ext = os.path.splitext(source)
    target = 'media/videos_uploaded/360p/' + os.path.basename(base) + '_360p' + ext
    os.makedirs(os.path.dirname(target), exist_ok=True)
    cmd = 'ffmpeg -i "{}" -vf scale=640:360 -c:v libx264 -threads 1 -crf 23 -c:a aac -strict -2 "{}"'.format(source, target)
    subprocess.run(cmd, shell=True)
    video = Video.objects.get(id=video_id)
    video.video_360p_path = target
    video.save()

@job
def getThumbnail(source, target):
    os.makedirs(os.path.dirname(target), exist_ok=True)
    cmd = 'ffmpeg -i "{}" -ss 00:00:01.000 -update true -frames:v 1 "{}"'.format(source, target)
    subprocess.run(cmd, shell=True)
