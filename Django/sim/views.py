from django.shortcuts import render,get_object_or_404
from urllib.request import build_opener, HTTPCookieProcessor, Request
from django.contrib.auth.models import User, Group
from daychangers.models import Orderbook, Margin
from rest_framework.response import Response
from rest_framework import generics
from rest_framework import status
import django_filters
from django_filters.rest_framework import DjangoFilterBackend
from .exception import CsrfExemptSessionAuthentication
from .serializers import OrderSerializer,OrderDetailSerializer, OrderCreateSerializer
from rest_framework.views import APIView
from rest_framework.authentication import SessionAuthentication , BasicAuthentication
from rest_framework_jwt.authentication import JSONWebTokenAuthentication
from rest_framework.decorators import api_view
from rest_framework.generics import (
    ListAPIView,
    RetrieveAPIView,
    UpdateAPIView,
    DestroyAPIView,
    CreateAPIView, 
    RetrieveUpdateAPIView, 
    ListCreateAPIView,RetrieveUpdateDestroyAPIView)
from rest_framework.permissions import (
    AllowAny,
    IsAuthenticated,
    IsAdminUser,
    IsAuthenticatedOrReadOnly
    )
from rest_framework.filters import SearchFilter,OrderingFilter

class PostListAPIView(ListAPIView):
    serializer_class = OrderSerializer
    permission_classes = [IsAuthenticated]
    authentication_classes = [BasicAuthentication,JSONWebTokenAuthentication]
    
    def get_queryset(self):
        #query=self.request.GET.get("client_id")
        queryset=Orderbook.objects.filter(client_id=self.request.user).order_by('id')
        return queryset
        
class DetailListAPIView(RetrieveAPIView):
    queryset=Orderbook.objects.all()
    serializer_class = OrderDetailSerializer
    lookup_field='id'
    lookup_url_kwarg="id"

class PostUpdateAPIView(RetrieveUpdateAPIView):
    queryset=Orderbook.objects.all()
    serializer_class = OrderSerializer
    lookup_field='id'
    lookup_url_kwarg="id"       

class PostDeleteAPIView(RetrieveUpdateDestroyAPIView):
    queryset=Orderbook.objects.all()
    serializer_class = OrderSerializer
    lookup_field='id'
    lookup_url_kwarg="id"   

class PostCreateAPIView(CreateAPIView):
    queryset=Orderbook.objects.all()
    serializer_class = OrderCreateSerializer
    permission_classes = [IsAuthenticated]
    authentication_classes = [BasicAuthentication,JSONWebTokenAuthentication]
    def perform_create(self,serializer):
        serializer.save(client_id=self.request.user)
            

class PermissionView(APIView):
    permission_classes = [IsAuthenticated]
    authentication_classes = [BasicAuthentication,JSONWebTokenAuthentication]

    def get(self, request,format=None):
        data = {
            'username': request.user.username,
            'password':request.user.password,

        }
        return Response(data)