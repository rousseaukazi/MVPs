from django.db import models

class Video(models.Model):
    video_id = models.CharField(max_length=36)
    link = models.URLField()
    ms_time = models.DecimalField()
    message = models.CharField(max_length=140)
