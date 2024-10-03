from rest_framework import permissions as p, status
from rest_framework.generics import (
    ListCreateAPIView,
    RetrieveUpdateDestroyAPIView, CreateAPIView,
)
from rest_framework.parsers import MultiPartParser, FormParser, FileUploadParser
from rest_framework.response import Response

from beanlibapi.core import (
    models as m,
    serializers as s,
)


# from beanlibapi.core.permissions import IsOwnerOrReadOnly


class BeanListCreateView(ListCreateAPIView):
    queryset = m.Bean.objects
    serializer_class = s.BeanSerializer
    permission_classes = [p.IsAuthenticatedOrReadOnly]


class BeanRetrieveUpdateDestroyView(RetrieveUpdateDestroyAPIView):
    queryset = m.Bean.objects
    serializer_class = s.BeanSerializer
    # permission_classes = [p.IsAuthenticatedOrReadOnly, IsOwnerOrReadOnly]
    permission_classes = [p.IsAuthenticatedOrReadOnly]


class BeanImageUploadView(CreateAPIView):
    permission_classes = [p.IsAuthenticated]
    parser_classes = [FileUploadParser]

    def create(self, request, *args, **kwargs):
        return Response(status=status.HTTP_201_CREATED)
