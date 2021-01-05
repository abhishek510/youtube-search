from django.db import models

# Create your models here.

class Videos(models.Model):
    title = models.CharField(max_length=100)
    video_id = models.CharField(max_length=20, primary_key=True)
    description = models.CharField(max_length=300)
    thumbnail_url = models.URLField(max_length=100)
    published_date = models.DateTimeField()

    def __str__(self):
        return self.title