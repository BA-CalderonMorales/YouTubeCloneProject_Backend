from django.db import models


# Create your models here.
class Comment(models.Model):
    videoId = models.CharField(max_length=25)
    userComment = models.CharField(max_length=500)
    like = models.IntegerField(default=0)
    dislike = models.IntegerField(default=0)
    originalComment = models.ForeignKey('youtube_app.Comment', on_delete=models.CASCADE, null=True)


