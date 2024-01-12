"""Portafolioproy32 URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path

from portafolioapp32.view_login import vista_login
from portafolioapp32.views import registrar_usuariov, show_dashboard_contractorv, show_dashboard_developerv, make_profile_developerv, upload_filev, download_filev, attach_projectv



urlpatterns = [
    path('admin/', admin.site.urls),


    path('login/', vista_login, name = 'loginin'),
    path('userregistration/', registrar_usuariov, name='register'),

    path('dashcontractor/', show_dashboard_contractorv, name = 'dash_contractor'),
    path('dashdeveloper/', show_dashboard_developerv, name = 'dash_developer'),
    path('profiledev/', make_profile_developerv, name = 'make_profile_developer'),
    path('download/<pk>', download_filev, name='download_cv'),

    path('attachproject/', attach_projectv, name = 'make_project_attachment'),

   # path('uploadfiledev/', upload_filev, name = 'upload_dev'),





    #path('invitado/', vista_login, name = 'login_cuatro'),
]
