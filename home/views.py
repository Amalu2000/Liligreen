from django.shortcuts import render,redirect
from django.contrib.auth.models import User,auth

from .models import Products,Category,Review
from .forms import Reviewform,Productform
from django.contrib.auth.decorators import login_required, user_passes_test

# Create your views here.
def homefn(request):
     h=Products.objects.get(id=1)
     i=Products.objects.get(id=2)
     j=Products.objects.get(id=3)
     k=Products.objects.get(id=4)
     l=Products.objects.get(id=5)
     m=Products.objects.get(id=6)
     n=Products.objects.get(id=7)
     o=Products.objects.get(id=8)
     p=Products.objects.get(id=9)
     q=Products.objects.get(id=10)
     return render(request,'home.html',{'h':h,'i':i,'j':j,'k':k,'l':l,'m':m,'n':n,'o':o,'p':p,'q':q})

def registerfn(request):
     if request.method=='POST':        
         u=request.POST['username']
         e=request.POST['email']
         p=request.POST['number']
         p1=request.POST['password1']
         p2=request.POST['password2']
       
         if p1==p2: 
            if User.objects.filter(username=u).exists():
                return render(request,'register.html',{'err':'Username taken'})
            elif User.objects.filter(email=e).exists():
                return render(request,'register.html',{'err':'Email taken '})

            else:
                User.objects.create_user(username=u,email=e,last_name=p,password=p1)
                return redirect('/')
            
         else:
              return render(request,'register.html',{'err':'Password not matching'})
                     
          
     else:
          return render(request,'register.html')

def aboutfn(request):
     h=Products.objects.get(id=1)
     i=Products.objects.get(id=2)
     j=Products.objects.get(id=3)
     k=Products.objects.get(id=4)
     l=Products.objects.get(id=5)
     m=Products.objects.get(id=6)
     n=Products.objects.get(id=7)
     o=Products.objects.get(id=8)
     p=Products.objects.get(id=9)
     q=Products.objects.get(id=10)
     return render(request,'about.html',{'h':h,'i':i,'j':j,'k':k,'l':l,'m':m,'n':n,'o':o,'p':p,'q':q})  

def contactfn(request):
     h=Products.objects.get(id=1)
     i=Products.objects.get(id=2)
     j=Products.objects.get(id=3)
     k=Products.objects.get(id=4)
     l=Products.objects.get(id=5)
     m=Products.objects.get(id=6)
     n=Products.objects.get(id=7)
     o=Products.objects.get(id=8)
     p=Products.objects.get(id=9)
     q=Products.objects.get(id=10)
     return render(request,'contactus.html',{'h':h,'i':i,'j':j,'k':k,'l':l,'m':m,'n':n,'o':o,'p':p,'q':q})   

def productfn(request):
     x=Products.objects.all()
     h=Products.objects.get(id=1)
     i=Products.objects.get(id=2)
     j=Products.objects.get(id=3)
     k=Products.objects.get(id=4)
     l=Products.objects.get(id=5)
     m=Products.objects.get(id=6)
     n=Products.objects.get(id=7)
     o=Products.objects.get(id=8)
     p=Products.objects.get(id=9)
     q=Products.objects.get(id=10)
     return render(request,'products.html',{'xyz':x,'h':h,'i':i,'j':j,'k':k,'l':l,'m':m,'n':n,'o':o,'p':p,'q':q})



def productviewfn(request,p_id):
    if request.method=='POST':
        f=Reviewform(request.POST)
        if f.is_valid():
            x=f.save(commit=False)
            x.us=request.user
            a=Products.objects.get(id=p_id)
            x.product=a
            x.save()
            return redirect('/products')
    else:
        f=Reviewform()
        a=Products.objects.get(id=p_id)
        c=Review.objects.filter(product=p_id)
        x=Products.objects.all()
        h=Products.objects.get(id=1)
        z=Products.objects.get(id=2)
        j=Products.objects.get(id=3)
        k=Products.objects.get(id=4)
        l=Products.objects.get(id=5)
        m=Products.objects.get(id=6)
        n=Products.objects.get(id=7)
        o=Products.objects.get(id=8)
        p=Products.objects.get(id=9)
        q=Products.objects.get(id=10)
        return render(request,'productview.html',{'abc':a,'fm':f,'cmnts':c,'h':h,'z':z,'j':j,'k':k,'l':l,'m':m,'n':n,'o':o,'p':p,'q':q})



def loginfn(request):
    if request.method=='POST':
        u=request.POST['username']
        p1=request.POST['password1']
        x=auth.authenticate(username=u,password=p1)
        if x:
            auth.login(request,x)
            return redirect('/')
        
        else:
            return render(request,'login.html',{'err':'Inavlid username or password'})
      

    else:
        return render(request,'login.html')
    

def logoutfn(request):
    auth.logout(request)  
    return redirect('/')  

def is_admin(user):
    return user.is_superuser


@login_required(login_url='/login')
@user_passes_test(is_admin)
def addproductfn(request):
    if request.method=='POST':
        f=Productform(request.POST,request.FILES)
        if f.is_valid():
            x=f.save(commit=False)
            x.us=request.user
            x.save()
            return redirect('/products')
    else:
        f=Productform()
        return render(request,'addproduct.html',{'form':f,'x':'Add'})

def editfn(request,p_id):
    x=Products.objects.all()
    b=Products.objects.get(id=p_id)
    if b.us==request.user:
        if request.method=='POST':
            b=Products.objects.get(id=p_id)
            f=Productform(request.POST,request.FILES,instance=b)
            if f.is_valid():
                f.save()
                return redirect('/products')
        else:
            b=Products.objects.get(id=p_id)
            f=Productform(instance=b)
            return render(request,'edit.html',{'form':f,'x':'Edit','pqr':b}) 
    else:
        return redirect('/product')        

def deletefn(request,p_id):
     x=Products.objects.get(id=p_id)  
     x.delete()
     return redirect('/products') 