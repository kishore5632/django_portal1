from django.shortcuts import render,redirect
from .models import *
from django.contrib.auth.models import User
from django.contrib.auth import authenticate,login,logout
from .forms import *
from django.http import HttpResponse, HttpResponseRedirect
from django.contrib.auth.decorators import login_required
from django.contrib import messages
# Create your views here.
def index(request):
    messages.info(request, 'login successful')
    return render(request,'index.html')

def admin_login(request):
    return render(request,'admin_login.html')

def user_logout(request):
    logout(request)
    return redirect("user_login")

def job_list(request):
    jobs = JobPost.objects.all()
    context = {'jobs': jobs}
    return render(request,"joblist.html",context)

def user_login(request):
    if request.method == "POST":
        username = request.POST.get('uname')
        password = request.POST.get('pwd')
        user = authenticate(username = username , password = password)
        if user:
            login(request,user)
            return redirect("index")
        else:
            messages.info(request, 'Username OR password is incorrect')
    return render(request,'user_login.html')

def user_home(request):
    if not request.user.is_authenticated:
      return render(request,'user_home.html')

def apply(request):
    if request.method == 'POST':
        form = applyform(request.POST,request.FILES)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect('user_apply')    
    else:
        form = applyform()
        return render(request,'apply.html',{'form':form})


def user_signup(request):
    error = ""
    if request.method =='POST':
        f = request.POST['fname']
        l = request.POST['lname']
        p = request.POST['pwd']
        e = request.POST['Email']
        con = request.POST['Contact']
        try:
            user = User.objects.create_user(first_name=f,last_name=l, username=e, password=p)
            StudentUser.objects.create(user=user, mobile=con, type="student")
            error = "no"
        except:
            error = "yes"

    d ={'error':error}

    return render(request,'user_signup.html',d)