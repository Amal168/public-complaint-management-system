from django.shortcuts import render,redirect
from django.contrib.auth.models import User,Group
from django.contrib.auth import login,authenticate,logout
from django.contrib import messages

from myapp.models import *


# Create your views here.

def login_view(request):
    return render(request,'loginview.html')

def citizenupdate_view(request):
    a=Citizen.objects.get(LOGIN=request.user)
    return render(request,'citizen/citizenedit.html',{'data':a})

def citizensignup_view(request):
    return render(request,'citizen/citizensignup.html')

def citizen_home(request):
    a=Citizen.objects.get(LOGIN=request.user)
    return render(request,'citizen/citizonhome.html',{'data':a})

def citizenmain_page(request):
    a=Citizen.objects.get(LOGIN=request.user)
    return render(request,'citizen/citizenmainpage.html',{'data':a})

def citizen_signup(request):
    iname=request.POST['name']
    iemail=request.POST['email']
    ipassword=request.POST['password']
    imobile=request.POST['mobile']
    idob=request.POST['dob']
    igender=request.POST['gender']
    iplace=request.POST['place']
    idistrict=request.POST['district']
    ipincode=request.POST['pincode']
    iphoto=request.FILES['photo']
    b=User.objects.create_user(username=iemail,password=ipassword)
    b.groups.add(Group.objects.get(name='citizen'))
    a=Citizen()
    a.name=iname
    a.email=iemail
    a.mobile=imobile
    a.dob=idob
    a.gender=igender
    a.place=iplace
    a.district=idistrict
    a.pincode=ipincode
    a.photo=iphoto
    a.LOGIN=b
    a.save()
    messages.success(request,'signup scessful')
    return redirect('/myapp/login_view/')

# User.objects.get(username='aamir@gmail.com').delete()

def login_add(request):
    iuser=request.POST['user']
    ipassword=request.POST['password']
    if not iuser or not ipassword:
        messages.success(request,'login failed')
        return redirect('/myapp/login_view/')
    user=authenticate(request,username=iuser,password=ipassword)
    if user is not None:
        login(request,user)
        if user.groups.filter(name='citizen').exists():
            messages.success(request,'login scessful to citizon')
            return redirect('/myapp/citizenmain_page/')
        elif user.groups.filter(name='admin').exists():
            messages.success(request,'login scessful to govt office')
            return redirect('/myapp/govtoffice_home/')
        else:
            messages.success(request,'login failed')
            return redirect('/myapp/login_view/')
    else:
        messages.success(request,'login failed')
        return redirect('/myapp/login_view/')






def citizen_update(request):
    iname=request.POST['name']
    iemail=request.POST['email']
    imobile=request.POST['mobile']
    idob=request.POST['dob']
    igender=request.POST['gender']
    iplace=request.POST['place']
    idistrict=request.POST['district']
    ipincode=request.POST['pincode']
    a=Citizen.objects.get(LOGIN=request.user)
    a.name=iname
    a.email=iemail
    a.mobile=imobile
    a.dob=idob
    a.gender=igender
    a.place=iplace
    a.district=idistrict
    a.pincode=ipincode
    if 'photo' in request.FILES:
        iphoto=request.FILES['photo']
        a.photo=iphoto
        a.save()
    a.save()
    messages.success(request,'citizen is updated scussefully')
    return redirect('/myapp/citizen_home/')


def citizenchangepass_view(request):
    return render(request,'citizen/citizonchangepassword.html',)


def citizen_complaints(request):
    a=Complaint.objects.filter(CITIZEN__LOGIN=request.user)
    return render(request,'citizen/citizoncomplaint.html',{'data':a})


from datetime import datetime
def citizen_complaintsent(request):
    icomplaint=request.POST['complaints']
    a=Complaint()
    a.replay='pending'
    a.complaints=icomplaint
    a.date=datetime.now().date()
    a.CITIZEN=Citizen.objects.get(LOGIN=request.user)
    a.save()
    messages.success(request,'Complaint have been scessfully sent')
    return redirect('/myapp/citizen_complaints/')


def citizen_changepassword(request):
    inowpass=request.POST['nowpass']
    inewpass=request.POST['newpass']
    iCheckpass=request.POST['Checkpass']
    a=request.user
    if a.check_password(inowpass):
        if inewpass==iCheckpass:
            a.set_password(inewpass)
            a.save()
            messages.success(request,'password changed scessfully')
            return redirect('/myapp/login_view/')
        else:
            messages.success(request,'password changed failed')
            return redirect('/myapp/citizenchangepass_view')
    else:
        messages.success(request,'password changed failed')
        return redirect('/myapp/citizenchangepass_view')



def citizen_logout(request):
    logout(request)
    messages.success(request,'logout sucessfuly')
    return redirect('/myapp/login_view/')


    
def govtoffice_home(request):
    a=Citizen.objects.all()
    return render(request,'govtoffice/govtofficehome.html',{'data':a})

def govtchangepass_view(request):
    return render(request,'govtoffice/govtchangepassword.html')



def govt_changepassword(request):
    inowpass=request.POST['nowpass']
    inewpass=request.POST['newpass']
    iCheckpass=request.POST['Checkpass']
    a=request.user
    if a.check_password(inowpass):
        if inewpass==iCheckpass:
            a.set_password(inewpass)
            a.save()
            messages.success(request,'password changed scessfully')
            return redirect('/myapp/login_view/')
        else:
            messages.success(request,'password changed failed')
            return redirect('/myapp/govtoffice_home')
    else:
        messages.success(request,'password changed failed')
        return redirect('/myapp/govtoffice_home')

def govt_logout(request):
    logout(request)
    messages.success(request,'logout sucessfuly')
    return redirect('/myapp/login_view/')

def govtcomplaint_view(request):
    a=Complaint.objects.all()
    return render(request,'govtoffice/complaintsview.html',{'data':a})


def govtreplay_view(request,id):
    a=Complaint.objects.get(id=id)
    return render(request,'govtoffice/govtreplay.html',{'data':a})

def govt_replay(request):
    id=request.POST['id']
    ireplay=request.POST['replay']
    a=Complaint.objects.get(id=id)
    a.replay=ireplay
    a.save()
    return redirect('/myapp/govtcomplaint_view/')
    
