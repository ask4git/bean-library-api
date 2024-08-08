# from django.shortcuts import render
# from django.http import HttpResponse, JsonResponse
# from django.views.decorators.csrf import csrf_exempt
# from rest_framework import status
# from rest_framework.parsers import JSONParser
# from django.http import Http404
#
# from rest_framework.response import Response
# from rest_framework.views import APIView
from rest_framework import permissions as p, status
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.authtoken.models import Token

from django.contrib.auth import authenticate

from beanlibapi.core.permissions import IsOwnerOrReadOnly
from beanlibapi.core.serializers import BeanSerializer
from beanlibapi.core.models import Bean
from rest_framework.generics import (
    ListCreateAPIView,
    RetrieveUpdateDestroyAPIView,
)


class LoginView(APIView):
    def post(self, request):
        username = request.data.get('username')
        password = request.data.get('password')
        user = authenticate(username=username, password=password)
        if user:
            token, _ = Token.objects.get_or_create(user=user)
            return Response({
                'token': token.key,
                'user_id': user.pk,
                'username': user.username
            })
        else:
            return Response({'error': 'Invalid credentials'}, status=status.HTTP_400_BAD_REQUEST)


class BeanListCreateView(ListCreateAPIView):
    queryset = Bean.objects.all()
    serializer_class = BeanSerializer
    permission_classes = [p.IsAuthenticatedOrReadOnly]


class BeanRetrieveUpdateDestroyView(RetrieveUpdateDestroyAPIView):
    queryset = Bean.objects.all()
    serializer_class = BeanSerializer
    permission_classes = [p.IsAuthenticatedOrReadOnly, IsOwnerOrReadOnly]

# class BeanList(APIView):
#     def get(self, request, format=None):
#         beans = Bean.objects.all()
#         serializer = BeanSerializer(beans, many=True)
#         return Response(serializer.data)
#
#     def post(self, request, format=None):
#         serializer = BeanSerializer(data=request.data)
#         if serializer.is_valid():
#             serializer.save()
#             return Response(serializer.data, status=status.HTTP_201_CREATED)
#         return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
#
#
# class BeanDetail(APIView):
#     def get_object(self, pk):
#         try:
#             return Bean.objects.get(pk=pk)
#         except Bean.DoesNotExist:
#             raise Http404
#
#     def get(self, request, pk, format=None):
#         bean = self.get_object(pk)
#         serializer = BeanSerializer(bean)
#         return Response(serializer.data)
#
#     def put(self, request, pk, format=None):
#         bean = self.get_object(pk)
#         serializer = BeanSerializer(bean, data=request.data)
#         if serializer.is_valid():
#             serializer.save()
#             return Response(serializer.data)
#         return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
#
#     def delete(self, request, pk, format=None):
#         bean = self.get_object(pk)
#         bean.delete()
#         return Response(status=status.HTTP_204_NO_CONTENT)
