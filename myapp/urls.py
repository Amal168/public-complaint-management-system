"""
URL configuration for complaint project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.2/topics/http/urls/
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
from myapp import views

urlpatterns = [
    path('login_view/',views.login_view),
    path('login_add/',views.login_add),
    path('citizenmain_page/',views.citizenmain_page),
    path('citizenupdate_view/',views.citizenupdate_view),
    path('citizensignup_view/',views.citizensignup_view),
    path('citizen_signup/',views.citizen_signup),
    path('citizen_update/',views.citizen_update),
    path('citizen_home/',views.citizen_home),
    path('citizenchangepass_view/',views.citizenchangepass_view),
    path('citizen_changepassword/',views.citizen_changepassword),
    path('citizen_complaints/',views.citizen_complaints),
    path('citizen_complaintsent/',views.citizen_complaintsent),
    path('citizen_logout/',views.citizen_logout),

    path('govtoffice_home/',views.govtoffice_home),
    path('govtchangepass_view/',views.govtchangepass_view),
    path('govt_changepassword/',views.govt_changepassword),
    path('govt_logout/',views.govt_logout),
    path('govtcomplaint_view/',views.govtcomplaint_view),
    path('govtreplay_view/<id>',views.govtreplay_view),
    path('govt_replay/',views.govt_replay),
]
