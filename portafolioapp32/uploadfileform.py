
from django import forms
from portafolioapp32.models import Profile



class UploadFileForm(forms.ModelForm):
	class Meta:
		model=Profile
		fields=['cv',]