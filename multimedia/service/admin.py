from django.contrib import admin
from .models import Artist, Album, Track


class ArtistAdmin(admin.ModelAdmin):
    pass


admin.site.register(Artist, ArtistAdmin)


class AlbumAdmin(admin.ModelAdmin):
    pass


admin.site.register(Album, AlbumAdmin)


class TrackAdmin(admin.ModelAdmin):
    pass


admin.site.register(Track, TrackAdmin)