from rest_framework import serializers

from .models import Track, Author, Album, Albums


class TrackSerializer(serializers.ModelSerializer):
    author = serializers.SlugRelatedField(slug_field='name', queryset=Author.objects.all())

    class Meta:
        model = Track
        fields = ['id', 'title', 'author', "picture", "long"]

class MyPlaylistSerializer(serializers.ModelSerializer):
    tracks = TrackSerializer(many=True)
    class Meta:
        model = Album
        fields = ['tracks']

class AuthorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Author
        fields = ('id', 'name')

class AlbumSerializer(serializers.ModelSerializer):
    tracks = TrackSerializer(many=True)
    authors = AuthorSerializer(many=True)
    class Meta:
        model = Album
        fields = ['tracks', "title","authors", "picture", "type"]
class GetAlbumsSerializer(serializers.ModelSerializer):
    tracks = TrackSerializer(many=True)
    authors = AuthorSerializer(many=True)
    class Meta:
        model = Album
        fields = ['tracks', 'title', 'picture', 'authors', "type"]
