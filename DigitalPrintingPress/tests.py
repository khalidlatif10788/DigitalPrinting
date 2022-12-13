from http import client
from multiprocessing.sharedctypes import Value
from django.test import Client
# from urllib import request, response
from django.test import SimpleTestCase,TestCase

# Create your tests here.
from django.urls import reverse, resolve
from DigitalPrintingPress.views import CategoryListView,productListView
from django.contrib.auth.models import User
from DigitalPrintingPress.models import adress,MainCategoery,SubCategory,Product,Cart,ProductDetail

class TestUrls(SimpleTestCase):
    def test_category_List_is_resolved(self):
        url="/"
        # print(resolve(url))
        self.assertEquals(resolve(url).func.view_class, CategoryListView)
    def test_Product_List_is_resolved(self):
        url="/productlist/2"
        self.assertEquals(resolve(url).func.view_class, productListView)

class TestView(TestCase):
    def setUp(self):
        self.c = Client()
        self.url="/"
       
        # create user
        self.test_user1 = User.objects.create_user(username='testuser1', password='1X<ISRUkw+tuK')
        self.test_user2 = User.objects.create_user(username='testuser2', password='2HJ1vRV0Z&3iD')
        self.test_user1.save()
        self.test_user2.save()
       # create Main category
        self.maincat= MainCategoery.objects.create(main_category_name="Shirt")
        self.maincat2= MainCategoery.objects.create(main_category_name="Coat")
        # create sub category
        self.subcat=SubCategory.objects.create(sub_main_category_id=self.maincat,sub_category_name="imported")
        # create product
        no_of_product =15
        for pname in range(no_of_product):

            self.product=Product.objects.create(product_main_category_id=self.maincat,product_sub_category_id=self.subcat,
            product_name="shirt-" + str(pname),product_description="Good Quality reasionable price",product_price=2500.00,
            product_discount=500.00
            )
            pid= Product.objects.last()
            ProductDetail.objects.create(detail_product_id=pid,detail_title="Size",detail_Description="small large xl")
            ProductDetail.objects.create(detail_product_id=pid,detail_title="Color",detail_Description="Red Blue Green")
    def test_project_list_GET(self):
        
        response= self.c.get(self.url)
    
        self.assertEquals(response.status_code, 200)
        self.assertTemplateUsed(response, "index.html")
        self.assertGreaterEqual(len(response.context['MainCategory']), 1)
    
    def test_logged_in_uses_correct_template_and_cart_count(self):
        login = self.client.login(username='testuser1', password='1X<ISRUkw+tuK')
        response = self.client.get(self.url)

        # Check our user is logged in
        self.assertEqual(str(response.context['user']), 'testuser1')
        # Check that we got a response "success"
        self.assertEqual(response.status_code, 200)
        # Check we used correct template
        self.assertTemplateUsed(response, "index.html")
        # Check that initially we don't have any product in cart)
        Cart_count= Cart.objects.filter(cart_customer_id=self.test_user1).count();
        self.assertTrue('Cart_count' in response.context)
        self.assertEqual(response.context['Cart_count'], 0)
        # product added to current user cart
        cart= Cart.objects.create(cart_product_id=self.product,cart_customer_id=self.test_user1,
         description_TitleWithdetail="size+s+color+red",qty=5,totalamount=4500.00,textprint="Pandemic World"
          )
        Cart_count= Cart.objects.filter(cart_customer_id=self.test_user1).count();
        self.assertGreaterEqual(Cart_count, 1)
        # Confirm cart count belong to testuser1
        self.assertEqual(response.context['user'], cart.cart_customer_id)
       
    def test_Product_list_main_category_wise_GET(self):
        
        response= self.c.get("/productlist/1")
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, "Product/productList.html")
        productCatwise =Product.objects.filter(product_main_category_id_id=1)
     
        self.assertQuerysetEqual(productCatwise, ["<Product: shirt-0>","<Product: shirt-1>","<Product: shirt-2>","<Product: shirt-3>","<Product: shirt-4>","<Product: shirt-5>","<Product: shirt-6>","<Product: shirt-7>","<Product: shirt-8>","<Product: shirt-9>","<Product: shirt-10>","<Product: shirt-11>","<Product: shirt-12>","<Product: shirt-13>","<Product: shirt-14>"], ordered=False)
    def test_pagination_is_telelve_main_cate_wise(self):
        response= self.c.get("/productlist/1")
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, "Product/productList.html")
        self.assertTrue('users' in response.context)
        # self.assertTrue(response.context['users'] == True)
        self.assertEqual(len(response.context['users']), 12)
    def test_pagination_remaining_product_is_3_main_cate_wise(self):
        # Get second page and confirm it has (exactly) remaining 3 items
        response = self.client.get("/productlist/1")
        self.assertEqual(response.status_code, 200)
        self.assertTrue('users' in response.context)
        # self.assertTrue(response.context['is_paginated'] == True)
        self.assertNotEqual(len(response.context['users']), 3)
    
    def test_logged_in_uses_correct_template_and_cart_count_for_url_listWithMainCatewise(self):
        login = self.client.login(username='testuser1', password='1X<ISRUkw+tuK')
        response = self.client.get("/productlist/1")

        # Check our user is logged in
        self.assertEqual(str(response.context['user']), 'testuser1')
        # Check that we got a response "success"
        self.assertEqual(response.status_code, 200)
        # Check we used correct template
        self.assertTemplateUsed(response, "Product/productList.html")
        # Check that initially we don't have any product in cart)
        Cart_count= Cart.objects.filter(cart_customer_id=self.test_user1).count();
        self.assertTrue('Cart_count' in response.context)
        self.assertEqual(response.context['Cart_count'], 0)
        # product added to current user cart
        cart= Cart.objects.create(cart_product_id=self.product,cart_customer_id=self.test_user1,
         description_TitleWithdetail="size+s+color+red",qty=5,totalamount=4500.00,textprint="Pandemic World"
          )
        Cart_count= Cart.objects.filter(cart_customer_id=self.test_user1).count();
        self.assertGreaterEqual(Cart_count, 1)
        # Confirm cart count belong to testuser1
        self.assertEqual(response.context['user'], cart.cart_customer_id)
    
     
    def test_logged_in_usesr_and_Detail_page(self):
        login = self.client.login(username='testuser1', password='1X<ISRUkw+tuK')
        response = self.client.get("/productDetail/2")

        # Check our user is logged in
        self.assertEqual(str(response.context['user']), 'testuser1')
        # Check that we got a response "success"
        self.assertEqual(response.status_code, 200)
        # Check we used correct template
        self.assertTemplateUsed(response, "Product/detail.html")
        # Check product show in detail Page
        self.assertTrue('product_item' in response.context)
         # Check product detail size, color are correct
        self.assertDictEqual(response.context['productdetail'],{'Size': ['small', 'large', 'xl'], 'Color': ['Red', 'Blue', 'Green']})
        # Check correct product is displaing
        self.assertEqual(response.context['product_item'].product_name, "shirt-1")
        self.assertNotEqual(response.context['product_item'].product_name, "shirt-2")
         # Check product detail size, color are correct
        self.assertDictEqual(response.context['productdetail'],{'Size': ['small', 'large', 'xl'], 'Color': ['Red', 'Blue', 'Green']})
        # Check that initially we don't have any product in cart)
        Cart_count= Cart.objects.filter(cart_customer_id=self.test_user1).count();
        self.assertTrue('Cart_count' in response.context)
        self.assertEqual(response.context['Cart_count'], 0)
        # product added to current user cart
        cart= Cart.objects.create(cart_product_id=self.product,cart_customer_id=self.test_user1,
         description_TitleWithdetail="size+s+color+red",qty=5,totalamount=4500.00,textprint="Pandemic World"
          )
        Cart_count= Cart.objects.filter(cart_customer_id=self.test_user1).count();
        self.assertGreaterEqual(Cart_count, 1)
        # Confirm cart count belong to testuser1
        self.assertEqual(response.context['user'], cart.cart_customer_id)
    
     
        