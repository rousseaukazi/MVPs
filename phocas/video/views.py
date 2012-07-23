from django.http import HttpResponse
from models import Video
from uuid import uuid4
import json

def new_video(request):
    link = request.POST['link']
    ms_time = request.POST['time']
    message = request.POST['message']
    video = Video.objects.create(video_id=str(uuid4()), link=link, ms_time=ms_time, message=message)
    return HttpResponse(video.video_id)

def get_video(request, video_id):
    video = Video.objects.get(video_id=video_id)
    info = {'link' : viedeo.link, 'ms_time' : video.ms_time, 'message' : video.message}
    return HttpResponse(json.dumps(info))
