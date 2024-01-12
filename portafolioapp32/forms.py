from django import forms
from portafolioapp32.models import Usuario

class LoginForm(forms.Form):
	nickname = forms.CharField(max_length = 255)
	password=forms.CharField(widget=forms.PasswordInput())


	class Meta:
	        model = Usuario
	        fields = ('nickname', 'password' )