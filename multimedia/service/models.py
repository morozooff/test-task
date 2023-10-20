from django.db import models

class Artist(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name

class Album(models.Model):
    name = models.CharField(max_length=255)
    year = models.PositiveIntegerField()
    artist = models.ForeignKey(Artist, on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.name}[{self.year}]"


class Track(models.Model):
    name = models.CharField(max_length=100)
    album = models.ForeignKey(Album, related_name='tracks', on_delete=models.CASCADE)

    def __str__(self):
        return self.name