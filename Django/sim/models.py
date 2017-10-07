from django.db import models
from django.dispatch import receiver
from django.db.models.signals import post_save
from rest_framework.authtoken.models import Token
from django.conf import settings

class Stockspecific(models.Model):
	""" Database model for gainer list """

	symbol = models.CharField(max_length=250)
	openPrice =models.DecimalField(max_digits=7, decimal_places=2)
	highPrice = models.DecimalField(max_digits=7, decimal_places=2)	
	ltp=models.DecimalField(max_digits=7, decimal_places=2)

	def __str__(self):
		return  self.symbol

class Orderbook(models.Model):
	client_id=models.CharField(max_length=100)
	symbol = models.CharField(max_length=250)
	price =models.DecimalField(max_digits=7, decimal_places=2)
	quantity = models.IntegerField()
	date =models.DateTimeField()

	def __str__(self):
		return  self.client_id		

@receiver(post_save,sender=settings.AUTH_USER_MODEL)
def create_auth_token(sender, instance=None, created=False, **kwargs):
    if created:
        Token.objects.create(user=instance)		
