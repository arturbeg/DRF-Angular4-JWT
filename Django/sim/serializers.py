from django.contrib.auth.models import User, Group 
from rest_framework import serializers
from daychangers.models import Orderbook

class OrderSerializer(serializers.ModelSerializer):
    class Meta:
        model = Orderbook
        fields = ('id','client_id', 'symbol','price','quantity','date','trade_type','orderno','ordertype','status' )    
           
class OrderDetailSerializer(serializers.ModelSerializer):
    class Meta:
        model = Orderbook
        fields = ('id','client_id', 'symbol','price','quantity','date','trade_type','orderno','ordertype','status' )   

class OrderCreateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Orderbook
        fields = ('symbol','price','quantity','date','trade_type','orderno','ordertype','status' )                                  