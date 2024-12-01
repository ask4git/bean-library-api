from os import environ

from django.http import JsonResponse
from rest_framework import permissions as p, status
from rest_framework.generics import (
    CreateAPIView,

)
from rest_framework.parsers import MultiPartParser, FormParser, FileUploadParser
from rest_framework.response import Response
from beanlibapi.apps.core.utils.aws import create_presigned_post
from beanlibapi.apps.core import serializers as s
from shortid import ShortId
import os

SID_GENERATOR = ShortId()


def generate_sid():
    return str(SID_GENERATOR.generate())


def renaming_file_with_uid(file_name: str):
    _file_name, ext = os.path.splitext(file_name)
    replaced_file_name = "".join(_file_name.replace(" ", "_").split())
    return f"media/{replaced_file_name}_{generate_sid()}{ext}"


class AttachmentUploadView(CreateAPIView):
    permission_classes = [p.IsAuthenticated]

    # parser_classes = [MultiPartParser]
    # serializer_class = s.AttachmentSerializer

    def post(self, request, *args, **kwargs):
        bucket_name = environ['AWS_S3_BUCKET_NAME']
        file_name = request.data.get('name')
        object_name = renaming_file_with_uid(file_name)
        data = create_presigned_post(bucket_name, object_name,
                                     fields={"Content-Type": request.data.get('format')},
                                     conditions=[
                                         {"Content-Type": request.data.get('format')}
                                     ])
        data.update({"name": object_name})
        return JsonResponse(data=data, status=status.HTTP_201_CREATED)


class AttachmentUploadConfirmView(CreateAPIView):
    permission_classes = [p.IsAuthenticated]
    serializer_class = s.AttachmentSerializer

    # def create(self, request, *args, **kwargs):
    #     print(request.data)
    #     return Response(status=status.HTTP_201_CREATED)
