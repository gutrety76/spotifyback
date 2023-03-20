from django.db import models


# Create your models here.
class Author(models.Model):
    name = models.CharField(max_length=255)

    def __str__(self):
        return self.name


class Album(models.Model):
    title = models.CharField(max_length=255)
    authors = models.ManyToManyField('Author')
    tracks = models.ManyToManyField('Track')
    picture = models.ImageField(upload_to="aLbumsimages")
    type = models.CharField(max_length=100)
    def __str__(self):
        return self.title


class Track(models.Model):
    title = models.CharField(max_length=255)
    author = models.ForeignKey(Author, on_delete=models.CASCADE)
    file = models.FileField(upload_to="tracks")
    picture = models.ImageField(upload_to="images")
    long = models.TextField(max_length=10)

    def __str__(self):
        return self.title


class Albums(models.Model):
    albums = models.ManyToManyField('Album')
