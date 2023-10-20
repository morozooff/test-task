from rest_framework.routers import SimpleRouter
from .views import AlbumViewSet, ArtistViewSet, TrackViewSet
from django.urls import path
router = SimpleRouter()

router.register(r'albums', AlbumViewSet)
router.register(r'artists', ArtistViewSet)
router.register(r'tracks', TrackViewSet)

urlpatterns = router.urls

