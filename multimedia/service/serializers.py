from rest_framework import serializers
from .models import Artist, Album, Track


class ArtistSerializer(serializers.ModelSerializer):
    class Meta:
        model = Artist
        fields = ('name', )

class TrackSerializer(serializers.ModelSerializer):
    album_name = serializers.CharField(source='album.name')

    class Meta:
        model = Track
        fields = ('name', 'album_name')

    def to_representation(self, instance):
        res = super().to_representation(instance)
        nres = res.__class__()
        for k, v in res.items():
            if '_' in k:
                k = k.replace('_', '@')
            nres[k] = v
        return nres

    def create(self, validated_data):

        album_data = validated_data.pop('album')
        album = Album.objects.get(name = album_data['name'])
        track_created = Track.objects.create(name = validated_data.pop('name'), album = album )

        return track_created


    def update(self, instance, validated_data):

        album_data = validated_data.pop('album')
        album = Album.objects.get(name = album_data['name'])

        track = Track.objects.filter(id = instance.id)
        track.update(name = validated_data.pop('name'), album =album)
        track = Track.objects.get(id=instance.id)
        return track


class AlbumReadSerializer(serializers.ModelSerializer):
    album = serializers.SerializerMethodField()
    artist_name = serializers.CharField(source='artist.name')
    tracks = serializers.StringRelatedField(many=True, read_only=True)

    class Meta:
        model = Album
        fields = ('album', 'name', 'artist_name', 'tracks')


    def get_album(self, obj):
        return obj.__str__()

    def to_representation(self, instance):
        res = super().to_representation(instance)
        nres = res.__class__()
        for k, v in res.items():
            if '_' in k:
                k = k.replace('_', '@')
            nres[k] = v
        return nres


class AlbumWriteSerializer(serializers.ModelSerializer):
    artist_name = serializers.CharField(source='artist.name')

    class Meta:
        model = Album
        fields = ('name', 'year', 'artist_name',)

    def create(self, validated_data):

        artist_data = validated_data.pop('artist')
        artist = Artist.objects.get(name = artist_data['name'])

        album_created = Album.objects.create(name=validated_data.pop('name'), year=validated_data.pop('year'),
                                             artist=artist)


        return album_created


    def update(self, instance, validated_data):

        artist_data = validated_data.pop('artist')
        artist = Artist.objects.get(name=artist_data['name'])

        album = Album.objects.filter(id=instance.id)
        album.update(name=validated_data.pop('name'), year=validated_data.pop('year'), artist = artist)
        album = Album.objects.get(id=instance.id)
        return album