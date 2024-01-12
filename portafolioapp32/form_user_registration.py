
from django import forms
from portafolioapp32.models import Usuario

from django.forms import widgets
from datetime import date, datetime
from django_countries.data import COUNTRIES


class UsuarioForm(forms.ModelForm):
	
	class Meta:
		model = Usuario
		fields = [
			'name',
			'lastname',
			'nickname',
			'password',
			'rol',
			#'remote_work',
			#'country',
			#'salary',
			#'cv',




		]
		labels = {

			'name': 'Name',
			'lastname': 'Lastname',
			'nickname': 'Nickname',
			'password': 'Password',
			'rol': 'Role',
			'country': 'Country',
			'remote_work':'Remote_work',
			'country':'Country',
			'salary':'Salary',
			#'cv':'Resume',
		
		}	
		'''
		widgets = {
			'name': forms.TextInput(attrs={'class': 'form = control', 'id': 'name_id', 'required': True, 'placeholder': 'Type your name...'}),
			'lastname': forms.TextInput(attrs={'class': 'form = control', 'id': 'lastname_id', 'required': True, 'placeholder': 'Type your lastname...'}),
			'nickname': forms.TextInput(attrs={'class': 'form = control', 'id': 'nickname_id', 'required': True, 'placeholder': 'Type your nick...'}),
			'password': forms.PasswordInput(attrs={'class': 'form = control','required': True, 'placeholder': 'Type your password...'}),
			'rol': forms.Select(attrs={'class': 'form = control', 'id': 'role_id','required': True, 'placeholder': 'Select your rol...'}),
			#'country': forms.ChoiceField(sorted(COUNTRIES))
					
		}'''