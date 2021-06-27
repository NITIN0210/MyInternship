from django.shortcuts import render
from django.shortcuts import redirect
from django.http import HttpResponse
#database Register
from .models import Register

# Create your views here.
def home(request):
	return HttpResponse("HelloWorld!! ")

def htmlTags(req):
	return HttpResponse("<h2>html tag</h2><a href='https://localhost:8080/admin/'>hii</a>")

def userNameDisplay(request,uname):
	return HttpResponse("<h1>Hi! Welcome Mr/Mrs.<span style='color:green'>{}</span></h1>".format(uname))

def detailsDisplay(req,uname,age):
	return HttpResponse("<h2 style='text-align:center;padding:23px;background-color:aqua'>Hi Mr/Mrs. <span style='color:yellow'>{}</span>your Age is<span style='color:red'>  {}</span></h2>".format(uname,age))

def employeDisplay(req,eid,ename,eage):
	return HttpResponse("<script>alert('Hi {}')</script><h3> Hi Welcome Mr/Mrs.{} your age is {} your id is {}</h3>".format(ename,ename,eage,eid))

def htmlFileRender(req):
	return render(req,"html/sample.html")

def sampleHtml(req,name):
	return render(req,"html/sampleHtml.html",{"n":name})

def multiHtml(req,age,name):
	d={'n':name,'a':age}
	return render(req,"html/abc.html",{'n':name,'a':age})#d

def studentDetails(req):
	return render(req,"html/std.html")

def internalJS(req):
	return render(req,"html/internalJS.html")

def registrationForm(req):
	if req.method=="POST":
		uname=req.POST['uname']
		rollno=req.POST.get('rollno')
		email=req.POST['email']
		print("namemYYY= ",uname)
		print(req.POST)
		d={'username':uname,'rollno':rollno,'email':email}
		return render(req,'html/displayFormValues.html',d)

	return render(req,"html/myForm.html")
def htmlFormTask(req):
	if req.method=="POST":
		#print(req.POST['name'])
		d={'name':req.POST['name'],'gender':req.POST['gender'],'languagesKnown':req.POST.getlist('lknown'),'abcdef':req.POST['abc']}
		
		return render(req,'html/htmlFormControlsValues.html',d)
	return render(req,'html/htmlFormControls.html')
def bootstarpfun(req):
	return render(req,"html/sampleBootstrap.html")
def btrg(req):
	if req.method=="POST":
		d={'name':req.POST['name'],'gender':req.POST['gender'],'languagesKnown':req.POST.getlist('lknown'),'abcdef':req.POST['abc']}
		return render(req,'html/btrgValues.html',d)
	return render(req,"html/bootStrapRegistration.html")

def register2(req):
	if(req.method=="POST"):
		htmlName=req.POST['name']
		htmlEmail=req.POST['email']
		reg=Register(name=htmlName,email=htmlEmail)
		reg.save()
		return HttpResponse("insert success")
	return render(req,'html/dbOp.html')

def register1(req):
	#name=
	#email=
	#save insertion
	reg=Register(name="tinny",email="tinny@gmail.com")
	reg.save()
	return HttpResponse('<h2>Row Inserted/Saved successfully</h2>')

def displayRegister(req):
	data=Register.objects.all()
	return render(req,"html/displayRegister.html",{'data':data})
def singleView(req,y):
	w=Register.objects.get(id=y)
	n=w.name
	e=w.email
	return render(req,'html/sview.html',{'y':w})
	#return HttpResponse("<h2> your id is {}, <hr> your name is {}, <hr>email is:{}</h2>".format(y,n,e))
def singleUpdate(req,y):
	t=Register.objects.get(id=y)
	if req.method=="POST":
		name=req.POST["name"]
		email=req.POST['email']

		t.name=name
		t.email=email
		print("debugging",t.name,t.email)
		t.save()
		return redirect('/displayRegister')#original url not name

	return render(req,"html/singleUpdate.html",{'row':t})
def singleDelete(req,y):
	t=Register.objects.get(id=y)
	if req.method=="POST":
		if t.name==req.POST['name']:
			t.delete()
		return redirect('/displayRegister')
	return render(req,"html/singleDelete.html",{'row':t})