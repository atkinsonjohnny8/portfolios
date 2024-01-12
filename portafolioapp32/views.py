from django.shortcuts import render, get_object_or_404

# Create your views here.

from portafolioapp32.form_user_registration import  UsuarioForm
from portafolioapp32.make_profile import  ProfileForm
from portafolioapp32.projectform import  ProjectForm
from . models import Project, Messages, Usuario, Profile



from portafolioapp32.uploadfileform import  UploadFileForm
from django.shortcuts import render, redirect
from django.http import HttpResponse

from django.core.cache import cache






def registrar_usuariov(request, template_name='templates/crear_login.html'):
	
	
	form = UsuarioForm(request.POST)	
	
	if form.is_valid():
		
		form.save()
		form.clean()
	return render(request, template_name, {'form':form})

	

def show_dashboard_contractorv(request):
	q=Project.objects.all()
	
	template_name= 'templates/show_dashboard_contractor.html'
	return render(request, template_name, {'proj': q})



def show_dashboard_developerv(request):


	detalle=Project.objects.all()
	propietario = request.session.get('nickname')

	#detalle= get_object_or_404(Usuario, pk=pk)

	#dev = Project.objects.filter(lastname = Project.objects.get(nickname=propietario) )
	template_name='templates/show_dashboard_developer.html'

	return render(request, template_name, {'dash':detalle})
	#return render(request, template_name,{'dash':dev})



def make_profile_developerv(request):
	
	template_name='templates/myprofile.html'
		
	if request.method=='POST':
		form = ProfileForm(request.POST, request.FILES)
		if form.is_valid():
			
			form.save()
			#return redirect('dashdeveloper')
	else:
		form = ProfileForm()

	
	files = Profile.objects.all()	
	#context =  {'formx':form}

	data= dict()
	data['formx']= form
	data['files']= files	
	return render(request, template_name, data)



def download_filev(request, pk):
	uploaded_file=Profile.objects.get(pk=pk)
	response=HttpResponse(uploaded_file.file, content_type='application/force-download')
	response['Content-Disposition']=f'attachment;filename="{uploaded_file.file.name}"'
	return response



def attach_projectv(request):
	template_name='templates/attach_project.html'
		
	if request.method=='POST':
		form = ProjectForm(request.POST, request.FILES)
		if form.is_valid():
			
			form.save()
			#return redirect('dashdeveloper')
	else:
		form = ProjectForm()

	
	files = Project.objects.all()	
	#context =  {'formx':form}

	data= dict()
	data['formx']= form
	data['files']= files	
	return render(request, template_name, data)








def upload_filev(request):

	template_name='templates/myprofile.html'

	if request.method=='POST':
		form = UploadFileForm(request.POST, request.FILES)
		if form.is_valid():
			form.save()
			return redirect('uploadfiledev')

	else:
		form = UploadFileForm()

	files = Usuario.objects.all()
	
	data= dict()
	data['formx']= form
	data['files']= files

	return render(request, template_name, data)	
