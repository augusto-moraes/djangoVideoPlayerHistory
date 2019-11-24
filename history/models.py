from django.db import models


class modelUrl(models.Model):
    youtubeUrl = models.CharField(max_length=500)
