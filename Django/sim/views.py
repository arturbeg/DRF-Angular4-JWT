from django.shortcuts import render,get_object_or_404
from django.contrib.auth.models import User, Group
from rest_framework.renderers import JSONRenderer
from .serializers import UserSerializer, GroupSerializer, GainerSerializer, OrderSerializer
from .nse import Nse
from .models import Stockspecific,Orderbook
from rest_framework.response import Response
from rest_framework import status
from rest_framework.views import APIView
from rest_framework.decorators import api_view



class work(APIView):

    @api_view(['GET','POST'])
    def UserViewSet(request):
        """
        API endpoint that allows users to be viewed or edited.
        """

        queryset = User.objects.all().order_by('-date_joined')
        serializer_class = UserSerializer(queryset,many=True)
        return Response(serializer_class.data)

    @api_view(['GET'])
    def GroupViewSet(request):
        """
        API endpoint that allows groups to be viewed or edited.
        """
        queryset = Group.objects.all()
        serializer_class = GroupSerializer(queryset,many=True)
        return Response(serializer_class.data)

    @api_view(['GET','POST'])
    def Gainer(request):
    """ Updating the top gainer list in real time """
        nse = Nse()
        gainer=nse.get_top_gainers()
        value=Stockspecific.objects.all()
        if value:
            i=1
            for stock in gainer:
                obj = Stockspecific.objects.get(id=i)
                obj.symbol =stock['symbol']
                obj.highPrice=stock['highPrice']
                obj.ltp=stock['ltp']
                obj.save()
                i=i+1
        else:    
            for stock in gainer:
                query=Stockspecific(symbol=stock['symbol'],openPrice=stock['openPrice'],highPrice=stock['highPrice'],ltp=stock['ltp'])
                query.save()

        queryset=Stockspecific.objects.all()
        serializer_class = GainerSerializer(queryset,many=True)
        return Response(serializer_class.data)

    @api_view(['GET','PUT', 'DELETE', 'PATCH'])   
    def data(request):
        """ Fetching the order book of user """
        user = request.user
        queryset=Orderbook.objects.filter(client_id=user)    
        serializer_class = OrderSerializer(queryset,many=True)
        return Response(serializer_class.data)