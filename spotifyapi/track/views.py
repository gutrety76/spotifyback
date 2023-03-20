from django.shortcuts import render
from rest_framework import generics
from rest_framework.response import Response

# Create your views here.
from .models import *
from .serializer import TrackSerializer, AuthorSerializer, MyPlaylistSerializer, AlbumSerializer, GetAlbumsSerializer


class TrackAPIView(generics.ListAPIView):
    queryset = Track.objects.all()
    serializer_class = TrackSerializer


class GetAlbumsAPIView(generics.ListAPIView):
    queryset = Album.objects.exclude(title='Мой плейлист')
    serializer_class = GetAlbumsSerializer


class AuthorAPIView(generics.ListAPIView):
    queryset = Author.objects.all()
    serializer_class = AuthorSerializer


class MyPlaylistAPIView(generics.ListAPIView):
    queryset = Album.objects.filter(title='Мой плейлист')
    serializer_class = MyPlaylistSerializer


from django.http import HttpResponse
from rest_framework.views import APIView


class search_albums(APIView):

    def get(self, request, title):
        # playlist_id is the value from the URL
        # For example, if the URL is '/myplaylist/42/', playlist_id will be 42
        playlist = Album.objects.get(title=title)
        serializer = AlbumSerializer(playlist)
        return Response(serializer.data)


class TrackRetrieveView(APIView):
    def get(self, request, pk):
        track = Track.objects.get(pk=pk)
        file = track.file

        # Open the file in binary mode
        with open(file.path, 'rb') as f:
            response = HttpResponse(f.read(), content_type='audio/mpeg')
            return response
