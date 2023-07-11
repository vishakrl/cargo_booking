from django.shortcuts import render,redirect
from django .http import HttpRequest
from django.contrib import auth
from django.contrib.auth.models import User
from .models import order
from .models import booking

# Create your views here.

def index(request):
    return render(request,'index.html')



def about(request):
    return render(request,'about.html')


def book(request):

    # cargotype=[{'name':'International'}, {'name':'Domestic'}]
    if request.method=='POST':
        
        sname=request.POST['sname']
        rname=request.POST['rname']
        dest=request.POST['dest']
        address=request.POST['address']
        c_type=request.POST['c_type']
        weight=request.POST['weight']
        
        date=request.POST['date'] 
        ctno=request.POST['ctno']

        c_obj=order.objects.create(s_name=sname,r_name=rname,dst=dest,address=address,cargo_type=c_type,weight=weight,price=0,date=date,ctno=ctno)
        c_obj.save()
        # msg='Cargo booking succesfull '
        return redirect('/')
    else:
         return render(request,'booking.html')
    


def login(request):
    if request.method=='POST':
        uname=request.POST['uname']
        pword=request.POST['pword' ]
        user=auth.authenticate(username=uname,password=pword)
        if user:

            
            auth.login(request,user)
            
            return redirect('/')
            
        msg='invalid user name and password'  
        return render(request,'login.html',{'msg':msg})
    else:
        return render(request,'login.html')
    


def register(request):
    if request.method=='POST':
      uname=request.POST['uname']
      fname=request.POST['fname']
      lname=request.POST['lname']
      email=request.POST['email']
      pword=request.POST['pword']
      rpword=request.POST['rpword']
      if pword==rpword:
            if User.objects.filter(username=uname):
                msg="username is already taken"
                return render(request,'register.html',{'val':msg})
            elif User.objects.filter(email=email):
                msg="email is already taken"
                return render(request,'register.html',{'val':msg})
            
            else:
                user=User.objects.create_user(first_name=fname,last_name=lname,username=uname,email=email,password=pword) 
                user.save();
                auth.login(request,user) 
                return redirect("/")
                
      else:
            msg="invalid password"
            return render(request,'register.html',{'val':msg})
    else:
        return render(request,"register.html") 
    


def view_book(request):
    cargo_details=order.objects.filter(s_name=request.user.username)
    return render(request,'viewbook.html',{'c_details':cargo_details})
    
      
def over2(request):
    cargo=order.objects.all()
    return  render(request,'overviewbook.html',{'details':cargo})
         


def over_view(request):
    num=request.GET['numod']
    wt=request.GET['weight']
    nprice=int(wt)*20
    cargo_det=order.objects.get(orderno=num)
    cargo_det.price=nprice
    cargo_det.save()
    cargo=order.objects.all()
    return  render(request,'overviewbook.html',{'details':cargo})
         
         
    
         
        
     
         

    
     
   

def logout(request):
     auth.logout(request)
     return redirect('/')

