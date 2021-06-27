from django.shortcuts import render
from django.http import HttpResponse
from WebSite.models import UserData

# Create your views here.
def index(req):
	if req.method=="POST" and req.POST.get('SignIn'):
		email=req.POST['uname']
		pswd=req.POST['pswd']
		info=UserData.objects.get(email=email)
		if info.email==email and info.pswd==pswd:
			return render(req,'html/FirstPage.html',{'id':info.id})
	elif req.method=="POST" and req.POST.get('SignUp'):
		fname=req.POST['fname']
		lname=req.POST['lname']
		email=req.POST['email']
		mobile=req.POST['mobile']
		pswd=req.POST['pswd']
		ud=UserData.objects.create(fname=fname,lname=lname,email=email,mobile=mobile,pswd=pswd)
		return render(req,'html/index.html')
	return render(req,'html/index.html')