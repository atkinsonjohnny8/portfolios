
from django import forms
from portafolioapp32.models import  Profile

from django.forms import widgets
from datetime import date, datetime
from django_countries.data import COUNTRIES


class ProfileForm(forms.ModelForm):
	
	class Meta:
		model = Profile
		fields = [
			'nickname',
			'country',
			'remote_work',
			'salary',
			'cv',
		
		]


		labels = {

			'nickname':'Nickname',
			'country': 'Country',
			'remote_work': 'Remote work',
			'salary': 'Salary range',
			'cv': 'Resume',

		}	
		



		widgets = {
			'name': forms.TextInput(attrs={'class': 'form = control', 'id': 'name_id', 'required': True, 'placeholder': 'Type your name...'}),
			#'country': forms.ChoiceField(COUNTRIES.items()),
			#'remote_work': forms.ChoiceField(REMOTE_WORK),
			#'salary': forms.ChoiceField(SALARY_RANGE),
			
					
		}