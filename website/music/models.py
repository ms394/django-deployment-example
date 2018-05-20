from django.db import models

# Create your models here.
class Album(models.Model):
    album_title = models.CharField(max_length=200)
    artist = models.CharField(max_length=100)
    genre = models.CharField(max_length=100)
    image = models.CharField(max_length=1000)

    def __str__(self):
        return self.album_title

class Song(models.Model):
    album=models.ForeignKey(Album,on_delete=models.CASCADE)
    song_title = models.CharField(max_length=200)
    file_type= models.CharField(max_length=10)

    def __str__(self):
        return self.song_title
