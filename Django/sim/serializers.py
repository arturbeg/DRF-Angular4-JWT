from django.contrib.auth.models import User, Group 
from rest_framework import serializers
from .models import Stockspecific, Orderbook


class UserSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = User
        fields = ('username', 'email', 'groups')


class GroupSerializer(serializers.ModelSerializer):
    class Meta:
        model = Group
        fields = ('url', 'name')

class GainerSerializer(serializers.ModelSerializer):
    class Meta:
    	model = Stockspecific
    	fields = ('symbol', 'openPrice','highPrice','ltp')

class OrderSerializer(serializers.ModelSerializer):
    class Meta:
    	model = Orderbook
    	fields = ('client_id', 'symbol','price','quantity','date' )    	
               