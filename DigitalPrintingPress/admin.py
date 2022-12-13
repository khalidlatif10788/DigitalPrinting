
# vim: set fileencoding=utf-8 :
from traceback import print_exception
from typing import List
from django.contrib import admin
from django.template.response import TemplateResponse
from . import models
from DigitalPrintingPress.form import productCustomForm
from django.urls import path

    

class SubCategoryAdmin(admin.StackedInline):
    model= models.SubCategory
    extra=1
    list_display = (
        'sub_category_id',
        'sub_main_category_id',
        'sub_category_name',
        'sub_category_photo',
    )
    list_filter = (
        'sub_category_name',
        
    )
    
class MainCategoeryAdmin(admin.ModelAdmin):
    inlines = [SubCategoryAdmin]

    list_display = (
        'main_category_id',
        'main_category_name',
        'main_category_photo',
       
    )
    list_filter = (
        'main_category_id',
        'main_category_name',
        'main_category_photo',
    )

  


class ProductDetailAdmin(admin.StackedInline):
    
    model= models.ProductDetail
    extra=1

    list_display = ('product_detail_id', 'detail_product_id','detail_title')
    list_filter = (
        'detail_product_id',
        'product_detail_id',
        'detail_product_id',
        'detail_title',
        
    )

    
class ProductAdmin(admin.ModelAdmin):
    inlines= [ProductDetailAdmin]
    class Media:
      
        js = ['https://ajax.googleapis.com/ajax/libs/jquery/3.6.0/jquery.min.js',
            'admin/js/customadmin.js']
    list_display = (   
        'product_id',
        'product_main_category_id',
        'product_sub_category_id',
        'product_name',
        'product_price',
        'product_discount',
        'product_photo',
    )
    list_filter = (
        'product_main_category_id',
        'product_sub_category_id',
        'product_name',
        
    )
    
    def get_urls(self):
        # admin_view = self.admin_site.admin_view
        urls = super().get_urls()
        my_urls = [
            # path('my_view/', self.my_view, name="add-custom"),
            path('my_ajax/', self.load_cities, name="ajax_load_cities"),
        ]
        return my_urls + urls
    def load_cities(self,request):
        from django.shortcuts import  render
        from django.http.response import JsonResponse
        maincat_id = request.GET.get('mainCategoryID')
        subCate =models.SubCategory.objects.filter(sub_main_category_id=maincat_id)
        subcatDic={}
        for sub in subCate:
            subcatDic.update({sub.sub_category_id:sub.sub_category_name})
            
        data ={ 
        'subCatDic':subcatDic
         }
        return JsonResponse(data)
    # def my_view(self, request):
    #         if request.method == 'POST':
    #             fm = productCustomForm(request.POST,request.FILES)
    #             if fm.is_valid():
    #                 fm.save()
    #                 return TemplateResponse(request, "admin/DigitalPrintingPress/product/")

    #         else:
    #             fm=productCustomForm()
        
    #             value=fm
    #             context = dict(
    #             self.admin_site.each_context(request),
    #             key=value,    
    #             )
            
    #         return TemplateResponse(request, "admin/DigitalPrintingPress/Product/change_form.html",context)

  

class CustomerAdmin(admin.ModelAdmin):

    list_display = (
        'customer_id',
        'customer_user',
        'name',
        'phone',
        'userid',
        
    )
    list_filter = (
        'customer_user',
        'customer_id',
        'customer_user',
        'name',
        'phone',
        
    )
    search_fields = ('name',)

class AddressAdmin(admin.ModelAdmin):

    list_display = (
        'adress_id',
        'Adress_customer_id',
        'shipping_address',
        
        
    )
    list_filter = (
        'adress_id',
        'Adress_customer_id',
        'shipping_address',
        
    )
    search_fields = ('shipping_address',)



class CartAdmin(admin.ModelAdmin):

    list_display = (
        'cart_id',
        'cart_product_id',
        'cart_customer_id',
        'description_TitleWithdetail',
        'qty',
        'totalamount',
        'textprint',
        'cart_photo',
    )
    list_filter = (
        'cart_id',
        'cart_product_id',
        'cart_customer_id',
        'description_TitleWithdetail',
        'qty',
        'totalamount',
        'textprint',
        'cart_photo',
    )
class OrderDetailAdmin(admin.StackedInline):
    model= models.OrderDetail
    extra=0

    list_display = ( 
        'order_detail_id',
        'order_detail_obj',
        'transcation_id',
        'order_detail_product_id',
        'order_detail_customer_id',
        'order_detail_description_TitleWithdetail',
        'order_detail_qty',
        'order_detail_totalamount',
        'order_detail_textprint',
        'order_detail_photo',
    )
    list_filter = (
        'order_detail_product_id',
          'transcation_id',
        
    )
    
class OrderAdmin(admin.ModelAdmin):
    inlines= [OrderDetailAdmin]
    list_display = (

        'order_id',
        'Order_transcation_id',
        'order_customer',
        'order_date',
        'Status',
        
    )
    list_filter = (
        'Status',
        'order_date',
        
    )



def _register(model, admin_class):
    admin.site.register(model, admin_class)
    
_register(models.Order, OrderAdmin)
# _register(models.OrderDetail, OrderDetailAdmin)
_register(models.MainCategoery, MainCategoeryAdmin)
# _register(models.SubCategory, SubCategoryAdmin)
_register(models.Product, ProductAdmin)
# _register(models.ProductDetail, ProductDetailAdmin)
# _register(models.Customer, CustomerAdmin)
# _register(models.Cart, CartAdmin)

_register(models.adress,AddressAdmin)
