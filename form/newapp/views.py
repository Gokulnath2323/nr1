from django.shortcuts import render
from .models import users


# Create your views here.
def show(request):
     if request.method=="POST":
          name = request.POST["user"]
          password = request.POST["pass"]
          u = users(name= name,password=password)
          u.save()

     return render(request,'formapp/temp.html')
