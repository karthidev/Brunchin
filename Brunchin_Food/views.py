from django.shortcuts import redirect, render
from django.http import HttpResponse
from django.template import loader
from django.contrib.auth.models import User
from .models import foot_category,brunch_cart
from django.contrib.auth import authenticate, login ,logout
from django.http.response import JsonResponse
from django.db.models import Sum, Max, Min, Count, Avg
import razorpay
from django.db.models import Q
from django.core import serializers
# Create your views here.
def Brunc_idex(request):
 if 'user' in request.session:
    print("checked")
 else:
    print("notchecked") 
 food_items=foot_category.objects.all().values()
 context={
   'context':food_items
 }
 template = loader.get_template('index.html')
 return HttpResponse(template.render(context,request))

def userreg(request):
 context={}
 if request.method=='POST':
        uname=request.POST['uname'] 
        uemail=request.POST['uemail'] 
        ucpass=request.POST['upswd'] 
        if uname=="" or ucpass=="" or uemail=="":
            context['errmsg']="field cannot be empty"
            return render(request,'User/register.html',context)
        else:
             try:
                u=User.objects.create(username=uname,email=uemail)
                u.set_password(ucpass)
                u.save()
                uk=authenticate(username=uname,password=ucpass)
                request.session.set_expiry(300)
                if uk is not None:
                 login(request,uk)#start session and store id of logged in user session
                 context['success']="user created successfully"
                 return redirect('/')
             except Exception:
               
                context['errmsg']="user with same username alerady exist"
                return render(request,'User/register.html',context)
            #return HttpResponse("user created successfully")
 else:
        return render(request,'User/register.html')
    #return render(request,'registration.html')
  
  

def user_logout(request):
   logout(request)
   return redirect('/')


def user_login(request):
 context={}
 if request.method=='POST':
      uname=request.POST['uname'] 
      upass=request.POST['upswd'] 
      if uname=="" or upass=="":
            context['errmsg']="field cannot be empty"
            return render(request,'User/Login.html',context)
      else:
         request.session.set_expiry(300)
         u=authenticate(username=uname,password=upass)
         if u is not None:
                login(request,u)
                return redirect('/')
         else:
            context['errmsg']="invalid username and password"
            return render(request,'User/Login.html',context)
   
 return render(request,'User/Login.html')
  
def about_brunch(request):
      return render(request,'User/about.html')

def contact_brunch(request):
      return render(request,'User/contact.html')

def add_tocart(request,id):
    fo_carts=list(foot_category.objects.filter(id=id))
    for x in fo_carts:
      add_carts=brunch_cart.objects.create(userid=request.user.id,product_id=x.id,fo_name=x.food_name,fo_type=x.food_type,fo_price=x.food_price,fo_img=x.food_img)
      return redirect('/')

def getcartdetails(request):
    cart_cnt=brunch_cart.objects.count()
    return JsonResponse({'context': cart_cnt})

def viewcart_brunch(request):
    
      carts_details=brunch_cart.objects.all().values()
      cart_cnt=brunch_cart.objects.count()
      total=brunch_cart.objects.aggregate(Sum('fo_price'))
      
      context={
          'cart_data':carts_details,
          'cart_cnt':cart_cnt,
          'overall_price':total['fo_price__sum'],
      }
      return render(request,'cart.html',context)

def makepayment(request):
    context={}
    if request.user.is_authenticated:
        client = razorpay.Client(auth=("rzp_test_qPpA776V9DCblP", "TWcWQeLgGmHfG66yYcv7tzhJ"))
        data = { "amount": 10000000, "currency": "INR", "receipt": 'order_IluGWxBm9U8zJ8' }
        payment = client.order.create(data=data)
        return render(request,'Payment.html',context)
    else:
     context['errmsg']="Login and Move to Payment"
    return render(request,'User/Login.html',context)

def brunchfilter(request,fo_type):
  
    food_items=foot_category.objects.filter(food_type=fo_type).values()
    print(food_items)
    # context={
    # 'context':food_items
    # }
    return JsonResponse({'context':list(food_items)}, safe=False)


def getfocnt(request):
 food_cnt= list(brunch_cart.objects.values('product_id').annotate(fo_count=Count('product_id')))
 print(food_cnt)
 return JsonResponse({'context':food_cnt})