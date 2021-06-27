from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def home(req):
	return render(req,'app/home.html')

def about(req):
	return render(req,'app/about.html')
def contact(req):
	return render(req,'app/contact.html')