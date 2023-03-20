"""spotifyapi URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from django.conf import settings
from django.conf.urls.static import static
from track.views import TrackAPIView, AuthorAPIView, TrackRetrieveView, MyPlaylistAPIView, search_albums, \
    GetAlbumsAPIView

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/v1/trackslist', TrackAPIView.as_view()),
    path('api/v1/authorlist', AuthorAPIView.as_view()),
    path('api/v1/tracks/<int:pk>/', TrackRetrieveView.as_view(), name='track-retrieve'),
    path('api/v1/myplaylist', MyPlaylistAPIView.as_view()),
    path('api/v1/album/<str:title>', search_albums.as_view()),
    path('api/v1/albumslist',GetAlbumsAPIView.as_view())
]
if settings.DEBUG is True:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)