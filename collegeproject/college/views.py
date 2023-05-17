from django.contrib import messages
from django.contrib.auth.models import User
from django.shortcuts import render, get_object_or_404, redirect
from  . models import Department,Stream
from  . models import College
from  django.core.paginator import Paginator,EmptyPage,InvalidPage


# Create your views here.
def allStreamDept(request,c_slug=None):
    c_page=None
    streams_list=None
    if c_slug!=None:
        c_page=get_object_or_404(Department,slug=c_slug)
        streams_list=Stream.objects.all().filter(department=c_page)
    else:
        streams_list=Stream.objects.all().filter()

    return  render(request,"department.html",{'department':c_page})


def streamDetail(request,c_slug,stream_slug):
    try:
        stream=Stream.objects.get(department_slug=c_slug,slug=stream_slug)
    except Exception as e:
        raise e
    return  render(request,"stream.html",{'stream':stream})

def login(request):
    if request.method=="POST":
        username = request.POST.get('username',)
        password = request.POST.get('password', )

        college=College(username=username,password=password)
        college.save()


    return render(request,'login.html')

def register(request):
    if request.method=='POST':
        username=request.POST['username']
        password = request.POST['password']
        cpassword = request.POST['password1']
        if password==cpassword:
            if User.objects.filter(username=username).exists():
                messages.info(request,"Username Taken")
                return  redirect('register')

            else:
                user=User.objects.create_user(username=username,password=password)

                user.save();
                return  redirect('login')

        else:
            messages.info(request,"password not matched")
            return  redirect('register')
        return  redirect('/')
    return  render(request,"register.html")

def form(request):
    if request.method=='POST':
       college=College.objects.get()
       college.form()
       return redirect('/')
    return render(request,'form.html')
def confirm(request):
    if request.method=='POST':
       college=College.objects.get()
       college.confirm()
       return redirect('/')
    return render(request,'confirm.html')
