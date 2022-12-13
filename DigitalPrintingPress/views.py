
from audioop import reverse
import re
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import redirect, render
from django.urls import reverse_lazy
from django.views.generic import TemplateView,DetailView
from DigitalPrintingPress.models import MainCategoery,Product,ProductDetail,Cart,Customer,User,adress,SubCategory,Order
from DigitalPrintingPress import models
from django.views.generic import ListView,View
from django.views.decorators.csrf import csrf_exempt
from allauth.account.forms import SignupForm, LoginForm,AddEmailForm,ChangePasswordForm,SetPasswordForm,ResetPasswordForm,ResetPasswordKeyForm

from django.db.models import Q
from decimal import Decimal
from django.http.response import HttpResponse,JsonResponse
from django.utils.decorators import method_decorator
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from datetime import datetime,timedelta  
import hashlib
from allauth.account.views import SignupView, LoginView,PasswordSetView,PasswordChangeView,PasswordResetView,EmailView,ConfirmEmailView
from DigitalPrintingPress.form import CustomSignupForm,CustomLoginForm,AddressForm,MyCustomSetPasswordForm,MyCustomResetPasswordForm,MyCustomAddEmailForm
from django.db import DatabaseError, transaction
class indexView(TemplateView):
    template_name = "index.html"

class CategoryListView(ListView):
    model = MainCategoery
    context_object_name ='MainCategory'
    template_name='index.html'
    
    def get_context_data(self, **kwargs):
     context = super().get_context_data(**kwargs)
     if self.request.user.is_authenticated:
      customerid= User.objects.get(id=self.request.user.id)
      Cart_count= Cart.objects.filter(cart_customer_id=customerid).count();
      context['Cart_count'] = Cart_count
     return context
   
class productListView(View):
   template_name = 'Product/productList.html'
   category_Dec={}
   Cart_count=0
   paginate_by=12
   def get(self, request, *args, **kwargs):
    
    productCatwise=Product.objects.filter(product_main_category_id_id=self.kwargs['catid'])
          #pagination
    #user_list = User.objects.all()
    if request.user.is_authenticated:
        currentuser= request.user
        customerid= User.objects.get(id=currentuser.id)
        self.Cart_count= Cart.objects.filter(cart_customer_id=customerid).count();
    
    page = request.GET.get('page', 1)
    paginator = Paginator(productCatwise,12)
    try:
        users = paginator.page(page)
    except PageNotAnInteger:
        users = paginator.page(1)
    except EmptyPage:
        users = paginator.page(paginator.num_pages)

    #pagination end

    main_category= MainCategoery.objects.all()
    main_categorySingle=MainCategoery.objects.get(main_category_id=self.kwargs['catid'])
     
    for mainc in main_category:
      
      sub_category= SubCategory.objects.filter(sub_main_category_id=mainc)
      #for p in sub_category:
       #print(p.sub_category_id)
      self.category_Dec.update({mainc:sub_category})
    
    return render(request,self.template_name,{"users":users,"main_category":self.category_Dec,'Cart_count':self.Cart_count})

class SubCategoryListView(View):
    
 template_name = 'Product/productList.html'
 category_Dec={}
 Cart_count=0
 def get(self, request, *args, **kwargs):
    print(kwargs['sub_cat_id'])
    print(kwargs['main_cat_id'])

    productCatwise =Product.objects.filter(product_sub_category_id=self.kwargs['sub_cat_id'])
    if request.user.is_authenticated:
        currentuser= request.user
        customerid= User.objects.get(id=currentuser.id)
        self.Cart_count= Cart.objects.filter(cart_customer_id=customerid).count();
        #pagination
    #user_list = User.objects.all()
    
    page = request.GET.get('page', 1)
    print(page)
    paginator = Paginator(productCatwise,12)
    try:
        users = paginator.page(page)
    except PageNotAnInteger:
        users = paginator.page(1)
    except EmptyPage:
        users = paginator.page(paginator.num_pages)

    #pagination end
    main_category= MainCategoery.objects.all()
    
    # main_categorySingle=MainCategoery.objects.get(main_category_id=self.kwargs['main_cat_id'])
     
     
    for mainc in main_category:
      print(mainc)
      sub_category= SubCategory.objects.filter(sub_main_category_id=mainc)
      self.category_Dec.update({mainc:sub_category})
    return render(request,self.template_name,{"users":users,"main_category":self.category_Dec,'cart_count':self.Cart_count})

class AllProductListView(View):
    
 template_name = 'Product/productList.html'
 category_Dec={}
 Cart_count=0
 paginate_by = 12
 def get(self, request, *args, **kwargs):
    
    
    # productCatwise=Product.objects.filter(product_sub_category_id=self.kwargs['sub_cat_id'])
    main_category = MainCategoery.objects.all()
    if request.user.is_authenticated:
        currentuser= request.user
        customerid= User.objects.get(id=currentuser.id)
        self.Cart_count= Cart.objects.filter(cart_customer_id=customerid).count();
    allproduct = Product.objects.all()
    
    #pagination
    user_list = User.objects.all()
    page = request.GET.get('page', 1)
    print(page)
    paginator = Paginator(allproduct,12)
    try:
        users = paginator.page(page)
    except PageNotAnInteger:
        users = paginator.page(1)
    except EmptyPage:
        users = paginator.page(paginator.num_pages)

    #pagination end
    #main_categorySingle=MainCategoery.objects.get(main_category_id=self.kwargs['main_cat_id'])
     
     
    for mainc in main_category:
      print(mainc)
      sub_category= SubCategory.objects.filter(sub_main_category_id=mainc)
      self.category_Dec.update({mainc:sub_category})
    # 
    return render(request,self.template_name,{"main_category":self.category_Dec,'users': users,'Cart_count':self.Cart_count})




class ProductDetailView(View):
    description={}
    titleWithDes={}
    template_name = 'Product/detail.html'
    context_object_name ='pdetail'
    Cart_count=0
    
    
    def get(self, request, *args, **kwargs):
        self.description={}
        pro= Product.objects.get(product_id= self.kwargs['pk'])
        print(pro.product_id)
        if request.user.is_authenticated:
            currentuser= request.user
            customerid= User.objects.get(id=currentuser.id)
            self.Cart_count= Cart.objects.filter(cart_customer_id=customerid).count();

        pd= ProductDetail.objects.filter(detail_product_id=pro.product_id)
        for a in pd:
         print(a.detail_title)
         splitDescription=a.detail_Description.split(" ")
         self.description.update({a.detail_title:splitDescription})      
        
        return render(request,self.template_name,{"product_item":pro,"productdetail":self.description,'Cart_count':self.Cart_count})

@method_decorator(csrf_exempt, name='dispatch')
class AddToCart(View):
    def post(self, request):
    #   if request.user.is_authenticated:
        files = request.FILES
        product_image = files.get('product_image', None)
        productid= request.POST.get("productId")
        productDetail= request.POST.get("productDetail")
        productQtv= request.POST.get("productQtv")
        productTotalAmount= request.POST.get("productTotalAmount")
        productTextPrint= request.POST.get("productTextPrint")
        
        proid= Product.objects.get(product_id=productid)
        currentuser= request.user
        customerid= User.objects.get(id=currentuser.id)
        Cart_item_exist_check= Cart.objects.filter(Q(cart_customer_id=customerid.id) & Q(cart_product_id=proid))
        
        if(Cart_item_exist_check):
           p = Cart.objects.get(Q(cart_product_id=proid)& Q(cart_customer_id=customerid.id))
           p.qty += int(productQtv)
           p.totalamount= p.cart_product_id.product_price * p.qty
           p.save() 
           
           data ={ 
            'cartURL':"/goToCart/"
               }
           return JsonResponse(data)
           
        else:   
            cartobj = Cart(cart_product_id=proid,cart_customer_id=customerid,description_TitleWithdetail=productDetail,
                        qty=productQtv,totalamount=productTotalAmount,textprint=productTextPrint,cart_photo=product_image)
            cartobj.save()
              
            data ={ 
             'cartURL':"/goToCart/"
               }
            return JsonResponse(data)
      
        # return redirect(reverse_lazy('DigitalPrintingPress:login_custom'))
        #  return redirect('/login/') 
    

class goToCartListView(View):
    gtotal=Decimal(0.0)
    total_amount= Decimal(0.0)
    shippingCharges= Decimal(120.00)
    withoutShiping=0.00
    cartobj=""
    def get(self, request, *args, **kwargs):
        currentuser= request.user
        customerid= User.objects.get(id=currentuser.id)
        if Cart.objects.filter(cart_customer_id=customerid):
         self.cartobj= Cart.objects.filter(cart_customer_id=customerid)
      
         for tamount in self.cartobj:
            self.total_amount = self.total_amount + tamount.totalamount
            self.gtotal= self.total_amount + self.shippingCharges
        
        return render(request,"Product/cart.html",{'cartDetail':self.cartobj,'shippingCharges':self.shippingCharges,'total':self.total_amount,'withShipping':self.gtotal})
 
#    def get_queryset(self):
       
#         customerid= User.objects.get(id= request.user)
#         Cart_item_exist_check= Cart.objects.filter(Q(cart_customer_id=customerid) and Q(cart_product_id=proid))
#         return Cart.objects.filter(product_main_category_id_id=self.kwargs['catid'])

class UpdateCartIncreaeQty(View):

 def get(self, request, *args, **kwargs): 
      
      if(request.method == 'GET'):
        totala= Decimal(0.0)
        shippingCharges= Decimal(120.00)
        withoutShiping= Decimal(0.00)
        proid= request.GET['idq'] 
        p = Cart.objects.get(Q(cart_product_id=proid)& Q(cart_customer_id=request.user.id))
        p.qty += 1
        p.totalamount= p.cart_product_id.product_price * p.qty
        p.save()  
        #this is new start
        dat= Cart.objects.filter(cart_customer_id=request.user.id)
      
        for tamount in dat:
         totala += tamount.totalamount
        gtotal=totala + shippingCharges
        withoutShiping=totala
        #this is new end
        data ={ 
        'qty':p.qty,
        'total' : p.totalamount,
        'shippingCharges':shippingCharges,
        'withoutshipping':withoutShiping,
        'gtotal':gtotal

       
         }
      return JsonResponse(data)
class UpdateCartDecreaseQty(View):
    
 def get(self, request, *args, **kwargs): 
      
      if(request.method == 'GET'):
        totala= Decimal(0.0)
        shippingCharges= Decimal(120.00)
        withoutShiping= Decimal(0.00)
        proid= request.GET['idq'] 
        p = Cart.objects.get(Q(cart_product_id=proid)& Q(cart_customer_id=request.user.id))
        p.qty -= 1
        p.totalamount= p.cart_product_id.product_price * p.qty
        p.save()  
    
        dat= Cart.objects.filter(cart_customer_id=request.user.id)
      
        for tamount in dat:
         totala += tamount.totalamount
        gtotal=totala + shippingCharges
        withoutShiping=totala
        
        data ={ 
        'qty':p.qty,
        'total' : p.totalamount,
        'shippingCharges':shippingCharges,
        'withoutshipping':withoutShiping,
        'gtotal':gtotal

       
         }
      return JsonResponse(data)

class DeleteCartDecreaseQty(View):
    
 def get(self, request, *args, **kwargs): 
      
      if(request.method == 'GET'):
        totala= Decimal(0.0)
        shippingCharges= Decimal(120.00)
        withoutShiping= Decimal(0.00)
        proid= request.GET['idq']
        p = Cart.objects.get(Q(cart_product_id=proid)& Q(cart_customer_id=request.user.id))
        p.delete() 
        dat= Cart.objects.filter(cart_customer_id=request.user.id)
        for tamount in dat:
         totala += tamount.totalamount
        gtotal=totala + shippingCharges
        withoutShiping=totala
        
        data ={ 
        'qty':p.qty,
        'total' : p.totalamount,
        'shippingCharges':shippingCharges,
        'withoutshipping':withoutShiping,
        'gtotal':gtotal

       
         }
      return JsonResponse(data)



class  OrderDetailA(View):
   totala= Decimal(0.0)
   gtotal=Decimal(0.0)
   shippingCharges=Decimal(120.0)
#    detail = cart.objects.filter(user=user)
#    adr= adress.objects.filter(user=user)
#    for tamount in detail:
#          totala += tamount.totalAmount
#          gtotal=totala + shippingCharges
   
 
#    return render(request,"orderdetail.html",{'detail':detail,'totalamount':gtotal,'adr':adr})
    
   def get(self, request, *args, **kwargs):
        currentuser= request.user
        #userid= User.objects.get(id=currentuser.id)
        #customerid= Customer.objects.get(customer_id=userid.id)
        cartobj = Cart.objects.filter(cart_customer_id=request.user.id)
        adressobj= adress.objects.filter(Adress_customer_id=request.user.id)
        for tamount in cartobj:
          self.totala += tamount.totalamount
          self.gtotal=self.totala + self.shippingCharges
        return render(request,"Product/orderdetail.html",{"adress":adressobj,"cartobj":cartobj,'totalamount':self.gtotal})


class ProfileView(View):

    def get(self, request, *args, **kwargs):
        fm = AddressForm()
      
        return render(request,"profile/profile.html",{"fm":fm})
    def post(self, request, *args, **kwargs):
       fm = AddressForm(request.POST)
       currentuser= request.user
       userid= User.objects.get(id=currentuser.id)
       if fm.is_valid():
          obj = adress()
          obj.Adress_customer_id=userid
          obj.shipping_address = fm.cleaned_data['shipping_address']
          obj.save()
          return HttpResponseRedirect('/adress/')
          
       else:
            fm = AddressForm()
            return render(request,"profile/profile.html",{"fm":fm})



class ProfileOrder(View):

    def get(self, request, *args, **kwargs):
        currentuser= request.user
        userid= User.objects.get(id=currentuser.id)
        orderlist= Order.objects.filter(order_customer=userid)
        return render(request,"profile/order.html",{"orderlist":orderlist})

class AdressView(View):
    
    def get(self, request, *args, **kwargs):
        currentuser= request.user
        userid= User.objects.get(id=currentuser.id)
        # customerid= Customer.objects.get(customer_id=userid.id)
        adressobj= adress.objects.filter(Adress_customer_id=userid)
        return render(request,"profile/adressdes.html",{"adress":adressobj})

    def post(self, request):

        
        currentuser= request.user
        userid= User.objects.get(id=currentuser.id)
        # customerid= Customer.objects.get(customer_id=userid.id)
        adressobj= adress.objects.filter(Adress_customer_id=userid)
        return render(request,"profile/adressdes.html",{"adress":adressobj})

@method_decorator(csrf_exempt, name='dispatch')
class doChckout(View):
   
    def post(self, request):
        cartobj = Cart.objects.filter(cart_customer_id=request.user.id)
        pp_txn_dateTime= datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        transcation_id= "T"+ str(pp_txn_dateTime)   
       
        with transaction.atomic(): 
            if(cartobj):
                adress_to_delever_id= request.POST.get("AddressId")
                currentuser= request.user
                userid= User.objects.get(id=currentuser.id)
                totalamount= request.POST.get("totalAmount")
                status="Pending"
                
                orderobj= Order(Order_transcation_id=transcation_id,order_totalamount=totalamount,order_customer=userid,Status=status,adressid=adress_to_delever_id)
                orderobj.save()
                orderid_fororder=Order.objects.last()
            

                for cartitem in cartobj:
                    detailobj=models.OrderDetail(order_detail_obj=orderid_fororder,transcation_id=transcation_id,order_detail_product_id=cartitem.cart_product_id,order_detail_customer_id=cartitem.cart_customer_id,order_detail_description_TitleWithdetail=cartitem.description_TitleWithdetail,
                                order_detail_qty=cartitem.qty,order_detail_totalamount=cartitem.totalamount,order_detail_textprint=cartitem.textprint,order_detail_photo=cartitem.cart_photo)
                    detailobj.save()

                cartobj.delete()
                

            data={
             "purl":"/profile-order/"
               }
            return JsonResponse(data)
        # customer= request.user.id
        # order_total_amount= request.POST.get("totalAmount")
        # adress_to_delever_id= request.POST.get("AddressId")
      
        # pp_txn_dateTime= datetime.now().strftime("%m/%d/%Y")
        # present_time = datetime.now()       
        # expiry_date = datetime.now() + timedelta(hours=1)
        # expiryDate =expiry_date.strftime("%m/%d/%Y")
        # print(order_total_amount)
        # print(adress_to_delever_id)
        # #/////////transcation id
        # transcation_id= "T"+ str(pp_txn_dateTime) 
        # print(transcation_id)
        # HashedPassword =hashlib.sha1('x28094cu82'.encode('UTF-8'))

        # #////Post data
        # post_data={
        #                        "TRANSACTION_POST_URL": 'https://jazzcash.com.pk/CustomerPortal/TransactionManagement/DoTransactionViaSDK/',
        #                         #Merchant specific payment gateway base url
        #                         "INTEGERITY_SALT": 'c2973h0tvz', 
        #                         "merchantId": 'MC45537',
        #                         "merchantPassword":"x28094cu82",
        #                         "CURRENCY_CODE":"PKR",
        #                         "VERSION":"1.1",
        #                         "LANGUAGE":"EN",
        #                         "RETURN_URL":"127.0.0.1:8000/jazzcashResponse/",
        
        #                         "transactionRefNumber": transcation_id, 
        #                          "amount": order_total_amount, 
        #                          "transactionDateTime": pp_txn_dateTime, 
                                
        #                          "expiryDateTime": expiryDate,
        #                          "pp_TxnType":"MWALLET",
        # }

        # request.session["Trans_data"]=post_data
        # data={
        #    "purl":"/profile-order/"
        # }
        # return JsonResponse(data)
class jazzcashResponse(View):
    
   def get(self, request, *args, **kwargs): 
      
     
      return HttpResponse("order has been completed")
class TranscationCustom(View):
    
 def get(self, request, *args, **kwargs): 
     trans = request.session.pop('Trans_data', None)
     print(trans)
     
     return render(request,"Product/transcation.html",{"trans":trans})

# Handle 404 error

def error_404(request, exception):   
    context = {}   
    return render(request,'404.html', context)
def error_500(request):   
    context = {}   
    return render(request,'500.html', context)
                              


class CustomSignupView(SignupView):
    form_class = CustomSignupForm
    template_name = 'polls/account/signup.html'
    
    # def post(self, request):

    #     form = CustomSignupForm(request.POST)
    #     if form.is_valid():
    #         # process form data
    #         obj = Customer()
    #         obj.business_name = form.cleaned_data['business_name']
    #         obj.business_email = form.cleaned_data['business_email']
    #         obj.business_phone = form.cleaned_data['business_phone']
    #         obj.business_website = form.cleaned_data['business_website']
    #         #finally save the object in db
    #         obj.save()
    #         return HttpResponseRedirect('/')
    # success_url = "polls/login/"
    # AddEmailForm,ChangePasswordForm,SetPasswordForm,ResetPasswordForm,ResetPasswordKeyForm

from django.db.models import Q

class CustomloginView(LoginView):
    form_class = CustomLoginForm
    template_name = 'polls/account/login.html'
    # success_url = reverse_lazy('polls:index')
    redirect_field_name = "next"
class CustomPasswordChangeView(PasswordChangeView):
    form_class = ChangePasswordForm
    template_name = 'polls/account/password_change.html'
class CustomPasswordResetView(PasswordResetView):
    form_class = ResetPasswordForm
    template_name = 'polls/account/password_reset.html'
class CustomEmailView(EmailView):
    form_class = AddEmailForm
    template_name = 'polls/account/password_reset.html'
    
    

def SelectRelatedCategory():
    tuplist=[]
    GEEKS_CHOICES = tuplist
    sublist={}
    obj = MainCategoery.objects.get(main_category_id=1)
    subq = SubCategory.objects.filter(sub_main_category_id=obj)
        
    for sub in subq:
        cattuple=(sub.sub_category_id,sub.sub_category_name,)
        tuplist.append(cattuple)
        #  print(sub.sub_category_id)
        #  print(sub.sub_category_name)
        # print (sublist.sub_category_name)
        # print("-------------list tuplle---------------")
        # print(GEEKS_CHOICES)
    return tuplist
