from django.contrib.auth.models import User, Group,Permission
from django.db import models

class Orderbook(models.Model):
	client_id=models.CharField(max_length=100,null=True)
	symbol = models.CharField(max_length=250,null=True)
	price =models.DecimalField(max_digits=7, decimal_places=2, null=True)
	quantity = models.IntegerField(null=True)
	date =models.DateTimeField(null=True)
	trade_type=models.CharField(max_length=250,null=True)
	orderno=models.IntegerField(null=True)
	ordertype=models.CharField(max_length=100,null=True)
	status=models.CharField(max_length=100,null=True)

	def __str__(self):
		return  self.client_id