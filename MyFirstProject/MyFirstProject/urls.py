"""MyFirstProject URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.0/topics/http/urls/
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
from FirstApp import views
from WebSite import views as ws

urlpatterns = [
    path('admin/', admin.site.urls),
    ##########FirstApp
    ##admin,123
     #nitin,project@123
     #cmd:manage.py createsuperuser->to create user
    path('',views.home),#default page
    path('ht/',views.htmlTags),#empty parameter page

    path('und/<str:uname>/',views.userNameDisplay),
    path('dd/<str:uname>/<int:age>/',views.detailsDisplay),
    path('ed/<str:ename>/<int:eid>/<str:eage>/',views.employeDisplay),#with parameter

    path('html/',views.htmlFileRender),
    path('sample/<str:name>/',views.sampleHtml),
    path('multiParamHtml/<str:name>/<int:age>/',views.multiHtml),#html and html with paramater

    path('getStudent/',views.studentDetails),
    path('internalJS/',views.internalJS),

    path('registrationForm/',views.registrationForm,name='registrationForm1'),#html to html
    
    path('htmlFormTask/',views.htmlFormTask,name='htmlAction'),
    path('btstrp/',views.bootstarpfun),
    path('btrg/',views.btrg,name="btr"),

    path('register2/',views.register2,name='register2'),
    path('register1/',views.register1),

    path('displayRegister/',views.displayRegister,name="displayReg"),
    path('viw/<int:y>/',views.singleView,name="singleView"),
    path('update/<int:y>/',views.singleUpdate,name="singleUpdate"),
    path('delete/<int:y>/',views.singleDelete,name="singleDelete"),

    ##########WebSite
    path('index/',ws.index,name="sign")
]
