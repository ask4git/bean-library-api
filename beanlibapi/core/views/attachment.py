from rest_framework import permissions as p, status
from rest_framework.generics import (
    CreateAPIView,
)
from rest_framework.parsers import MultiPartParser, FormParser, FileUploadParser
from rest_framework.response import Response


class AttachmentUploadView(CreateAPIView):
    permission_classes = [p.IsAuthenticated]
    parser_classes = [MultiPartParser]

    def create(self, request, *args, **kwargs):
        print(request.FILES)
        return Response(status=status.HTTP_201_CREATED)
