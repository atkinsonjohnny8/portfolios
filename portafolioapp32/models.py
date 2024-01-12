from django.db import models

# Create your models here.

from django.conf import settings
from django.contrib.auth.models import AbstractBaseUser, BaseUserManager
from django_countries.fields import CountryField


class Usuario(models.Model):


	CONTRACTOR=1
	DEVELOPER=2

	ROL=(
		(CONTRACTOR, 'Contractor'),
		(DEVELOPER, 'Developer'),


		)


	name=models.CharField(max_length=255)
	lastname=models.CharField(max_length=255)
	nickname=models.CharField(max_length=255, primary_key=True)
	password=models.CharField(max_length=255)
	rol= models.PositiveSmallIntegerField(choices=ROL, blank=True, null=True)
	
	
	
	

	def check_password(self, password):
			return True
			if self.password == password:
				return True

		
					
	

class Project(models.Model):
	nickname=models.ForeignKey(Usuario, on_delete=models.CASCADE)
	projectname=models.CharField(max_length=255)
	
	abstract=models.TextField(max_length=255)
	projectfile=models.FileField(upload_to='projectuploads/')



class Messages(models.Model):
	sender=models.ForeignKey(Usuario, on_delete=models.CASCADE)
	receiver=models.CharField(max_length=255)
	messagetitle=models.CharField(max_length=255)
	messagebody=models.CharField(max_length=255)


class Profile(models.Model):

	YES=1
	NO=2
	REMOTE_WORK=(
		(YES, 'Yes'),
		(NO, 'No'),

		)


	JUNIOR=100
	SEMIJUNIOR=200
	SEMISENIOR=400
	SENIOR=1000

	SALARY_RANGE=(
		(JUNIOR, '100-200'),
		(SEMIJUNIOR, '200-400'),
		(SEMISENIOR, '400-1000'),
		(SENIOR,'1000-1200'),

		)

	nickname=models.ForeignKey(Usuario, on_delete=models.CASCADE)
	country=CountryField()
	remote_work= models.PositiveSmallIntegerField(choices=REMOTE_WORK, blank=True, null=True)
	salary=models.IntegerField(choices=SALARY_RANGE, blank=True, null=True)
	cv=models.FileField(upload_to='uploads/')
