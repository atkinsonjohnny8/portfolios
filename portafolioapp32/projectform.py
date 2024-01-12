
from django import forms
from portafolioapp32.models import  Project

from django.forms import widgets
from datetime import date, datetime



class ProjectForm(forms.ModelForm):
	
	class Meta:
		model = Project
		fields = [
			'nickname',
			'projectname',
			'abstract',
			'projectfile',
			
		
		]


		labels = {

			'nickname':'Nickname',
			'projectname': 'Project name',
			'abstract': 'Abstract',
			'projectfile': 'Project file',
			

		}	
		