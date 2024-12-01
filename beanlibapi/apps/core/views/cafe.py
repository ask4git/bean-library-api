from django.http import JsonResponse
from rest_framework.generics import UpdateAPIView, RetrieveUpdateDestroyAPIView, CreateAPIView
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework import permissions as p, status
from drf_rw_serializers.generics import (
    ListCreateAPIView,
)

from beanlibapi.apps.core.models import Cafe
from beanlibapi.apps.core.serializers import CafeSerializer, CafeDetailSerializer, CafeWriteSerializer
from beanlibapi.apps.core.permissions import IsOwnerOrReadOnly


class CafeView(ListCreateAPIView):
    queryset = Cafe.objects.all()
    serializer_class = CafeSerializer
    read_serializer_class = CafeSerializer
    write_serializer_class = CafeWriteSerializer
    permission_classes = [p.IsAuthenticatedOrReadOnly]

    def preform_create(self, serializer):
        serializer.save(owner=self.request.user)

    def post(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)

        if not serializer.is_valid():
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

        self.preform_create(serializer)
        return Response(serializer.data, status=status.HTTP_201_CREATED)


class CafeDetailView(UpdateAPIView):
    queryset = Cafe.objects.all()
    permission_classes = [IsOwnerOrReadOnly]
    serializer_class = CafeDetailSerializer
    lookup_field = 'uid'

    # def preform_create(self, serializer):
    #     serializer.save(owner=self.request.user)

    # def get_object(self):
    #     cafe = Cafe.objects.get(pk=self.kwargs['pk'])

    # def post(self, request, *args, **kwargs):
    #     print(kwargs.get('uid'))
    #     images = request.data.get('images')
    #     return Response({'images': images}, status=status.HTTP_200_OK)
