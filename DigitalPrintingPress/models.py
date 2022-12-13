from secrets import choice
from django.db import models
from datetime import datetime 


from django.contrib.auth.models import User

class MainCategoery(models.Model):

    main_category_id = models.AutoField(primary_key=True)
    main_category_name = models.CharField(max_length=100)
    main_category_photo=models.ImageField(upload_to='uploads/mainCategory',default='default.jpg')


    class Meta:
        db_table = 'main_category'
        indexes = [
            models.Index(fields=['main_category_id'],name='pk_main_category'),
        ]
    def __str__(self):
        return self.main_category_name

class SubCategory(models.Model):
    sub_category_id = models.AutoField(primary_key=True)
    sub_main_category_id = models.ForeignKey(MainCategoery,on_delete=models.CASCADE)
    sub_category_name = models.CharField(max_length=100)
    sub_category_photo=models.ImageField(upload_to='uploads/subCategory',default='default.jpg')

    class Meta:
        db_table = 'sub_category'
        indexes = [
            models.Index(fields=['sub_category_id'], name='pk_sub_category'),
            models.Index(fields=['sub_main_category_id'], name='fk_main_category')
        ]

    def __str__(self):
        return self.sub_category_name


class Product(models.Model):
   

    product_id = models.BigAutoField(primary_key=True)
    product_main_category_id = models.ForeignKey(MainCategoery,on_delete=models.CASCADE,default=3)
    product_sub_category_id = models.ForeignKey(SubCategory,on_delete=models.CASCADE)
    product_name = models.CharField(max_length=100)
    product_description = models.TextField(max_length=5000)
    product_price= models.DecimalField(max_digits=7,decimal_places=2)
    product_discount= models.DecimalField(max_digits=7,decimal_places=2,null=True)
    product_photo=models.ImageField(upload_to='uploads/product',default='default.jpg')
    
  
    class Meta:
        db_table = 'product'
        indexes = [
            models.Index(fields=['product_id'], name='pk_product'),
            models.Index(fields=['product_sub_category_id'], name='fk_sub_category'),
            models.Index(fields=['product_main_category_id'], name='fk_product_main_category'),
            
            
        ]

    def __str__(self):
        return self.product_name
    def related_subcate(self):
     
      return self.product_sub_category_id.get(product_main_category_id=self.product_main_category_id)

class ProductDetail(models.Model):
    product_detail_id = models.BigAutoField(primary_key=True)
    detail_product_id = models.ForeignKey(Product,on_delete=models.CASCADE)
    detail_title = models.CharField(max_length=1000)
    detail_Description = models.CharField(max_length=1000,default="")
    class Meta:
        db_table = 'product_detail'
        indexes = [
            models.Index(fields=['product_detail_id'], name='pk_product_detail'),
            models.Index(fields=['detail_product_id'], name='fk_product'),
            
        ]
    def __str__(self):
        return self.detail_title
    
        
    


class Customer(models.Model):
    customer_id = models.BigAutoField(primary_key=True)
    customer_user= models.ForeignKey(User, on_delete=models.CASCADE)
    name= models.CharField(max_length=50)
    phone= models.CharField(max_length=25)
    
    class Meta:
        db_table = 'customer'
        indexes = [
            models.Index(fields=['customer_id'], name='pk_user'),
           
        ]
    def __str__(self):
        return self.name
    def userid(self):
        return  self.customer_user.id


class adress(models.Model):
    adress_id = models.BigAutoField(primary_key=True)
    Adress_customer_id= models.ForeignKey(User, on_delete=models.CASCADE)
    shipping_address= models.TextField(max_length=500,null=True)
    class Meta:
        db_table = 'adress'
        indexes = [
            models.Index(fields=['Adress_customer_id'], name='pk_customer'),
           
        ]
    def __str__(self):
        return self.Adress_customer_id.username
    
    


class Cart(models.Model):
    cart_id = models.BigAutoField(primary_key=True)
    cart_product_id = models.ForeignKey(Product,on_delete=models.CASCADE)
    cart_customer_id = models.ForeignKey(User,on_delete=models.CASCADE)
    description_TitleWithdetail = models.TextField(max_length=3000, default="")
    qty= models.IntegerField()
    totalamount= models.DecimalField(max_digits=7,decimal_places=2,null=True)
    textprint=models.CharField(max_length=100,null=True)
    cart_photo=models.ImageField(upload_to = 'uploads/cart',null=True)


class Order(models.Model):
    order_status=(
    ("Pending", "Pending"),
    ("Processing", "Processing"),
    ("Delivered", "Delivered"),
    ("Completed", "Completed"),
    )
    order_id = models.BigAutoField(primary_key=True)
    Order_transcation_id = models.CharField(max_length=50, default="")
    order_totalamount = models.DecimalField(max_digits=7,decimal_places=2,null=True)
    order_customer = models.ForeignKey(User,on_delete=models.CASCADE)
    Status = models.CharField(max_length=20, choices=order_status)
    order_date = models.DateTimeField(default=datetime.now, blank=True)
    adressid= models.IntegerField()
    
class OrderDetail(models.Model):
    order_detail_id = models.BigAutoField(primary_key=True)
    order_detail_obj= models.ForeignKey(Order,on_delete=models.CASCADE)
    transcation_id = models.CharField(max_length=50, default="")
    order_detail_product_id = models.ForeignKey(Product,on_delete=models.CASCADE)
    order_detail_customer_id = models.ForeignKey(User,on_delete=models.CASCADE)
    order_detail_description_TitleWithdetail = models.TextField(max_length=3000, default="")
    order_detail_qty = models.IntegerField()
    order_detail_totalamount = models.DecimalField(max_digits=7,decimal_places=2,null=True)
    order_detail_textprint = models.CharField(max_length=100,null=True)
    order_detail_photo = models.ImageField(upload_to = 'uploads/orderDetail',null=True)
    
    
    
   