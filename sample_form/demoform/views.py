from django.shortcuts import render
from .models import User
# Create your views here.=
def form(request):
     if request.method=="POST":
          name = request.POST['username']
          passw = request.POST['password']
          u = User(name=name,password=passw)
          u.save()
     return render(request,'demo_form_app/temp.html')

