from django.shortcuts import render
from .models import Booknow
# Create your views here.
def index(request):
    return render(request,"index.html")


def booknow(request):
    if request.method=='POST':
        name=request.POST['name']
        email=request.POST['email']
        subject=request.POST['subject']
        message=request.POST['message']
        obj=Booknow()
        obj.name=name
        obj.email=email
        obj.subject=subject
        obj.message=message
        obj.save()
        return render(request,'index.html')
    else:
        return render(request,"Booknow.html")