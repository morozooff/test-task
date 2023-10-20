from django.shortcuts import render
from rest_framework import status
from rest_framework.decorators import action
from rest_framework.filters import OrderingFilter
from django_filters import rest_framework as filters
from rest_framework.generics import ListAPIView


from .serializers import AlbumReadSerializer, AlbumWriteSerializer, ArtistSerializer, TrackSerializer
from .models import Album, Artist, Track
from rest_framework.viewsets import ModelViewSet
from rest_framework.response import Response
from rest_framework.request import Request


class AlbumViewSet(ModelViewSet):
    queryset = Album.objects.all()

    filter_backends = [OrderingFilter]
    ordering_fields = ['name', 'artist', 'year']

    def get_serializer_class(self):
        if self.request.method == 'POST' or self.request.method == 'PUT':
            return AlbumWriteSerializer
        return AlbumReadSerializer

    def create(self, request, *args, **kwargs):

        serializer = self.get_serializer(data=request.data)
        if serializer.is_valid():
            self.perform_create(serializer)
            headers = self.get_success_headers(serializer.data)
            return Response({
                'message': 'Successfully created track',
                'data': serializer.data,
                'status': 'HTTP_201_CREATED',
            }, status=status.HTTP_201_CREATED, headers=headers)
        else:
            return Response({
                'message': 'Can not create',
                'data': serializer.errors,
                'status': 'HT',
            }, status=status.HTTP_400_BAD_REQUEST)



class ArtistViewSet(ModelViewSet):
    serializer_class = ArtistSerializer
    queryset = Artist.objects.all()

    filter_backends = [OrderingFilter]
    ordering_fields = ['name']

class TrackViewSet(ModelViewSet):
    queryset = Track.objects.all()
    serializer_class = TrackSerializer

    filter_backends = [OrderingFilter]
    ordering_fields = ['name', 'album']

    def create(self, request, *args, **kwargs):

        serializer = self.get_serializer(data=request.data)
        if serializer.is_valid():
            self.perform_create(serializer)
            headers = self.get_success_headers(serializer.data)
            return Response({
                'message': 'Successfully created track',
                'data': serializer.data,
                'status': 'HTTP_201_CREATED',
            }, status=status.HTTP_201_CREATED, headers=headers)
        else:
            return Response({
                'message': 'Can not create',
                'data': serializer.errors,
                'status': 'HT',
            }, status=status.HTTP_400_BAD_REQUEST)

