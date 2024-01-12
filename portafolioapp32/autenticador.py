from . models import Usuario
from django.shortcuts import get_object_or_404
from django.contrib.auth.hashers import check_password
import logging
#import appprototipo.view_login
import threading
from threading import Thread



	


def authenticatez(nickname, password):

	try:
				
		
		user = Usuario()
		
		
		usuario_auth = Usuario.objects.filter(nickname__startswith = '')	
		password_auth = Usuario.objects.filter(password__startswith = '')		
		if user.check_password(password_auth):
			return user
		else:
			return HttpResponse ("Incorrect user or password")
			#return None
	except Usuario.DoesNotExist:
			return HttpResponse ("There are no users yet")