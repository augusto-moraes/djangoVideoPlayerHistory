from django.db import models


class inputUrl(models.Model):
    youtubeUrl = models.CharField(max_length=500)
