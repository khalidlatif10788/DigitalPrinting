from django.urls import path ,include
from DigitalPrintingPress import views
from django.conf import settings
from django.conf.urls.static import static 
from django.contrib.auth.decorators import login_required
from django.conf.urls import handler404, handler500, handler403, handler400
handler404 = views.error_404 
from allauth.account.views import LogoutView
from django.contrib.auth.decorators import login_required
# handler500 = views.error_500
app_name="DigitalPrintingPress"
urlpatterns = [

   
    path('',views.CategoryListView.as_view(),name="categoryList"),
    path('profile/', login_required(views.ProfileView.as_view()),name="profile"),
    path('profile-order/', login_required(views.ProfileOrder.as_view()),name="profile-order"),
    path('adress/', views.AdressView.as_view(),name="adress"),
    path('summary/', login_required(views.OrderDetailA.as_view()),name="summary"),
    path('allProductlist/', views.AllProductListView.as_view(),name="allProductList"),
    path('productlist/<int:catid>', views.productListView.as_view(),name="productList"),
    path('subCatetlist/<int:sub_cat_id>/<int:main_cat_id>', views.SubCategoryListView.as_view(),name="subCatList"),
    path('productDetail/<int:pk>', login_required(views.ProductDetailView.as_view()),name="productDetail"),
    path('addToCart/', login_required(views.AddToCart.as_view()),name="AdtoCartitem"),
    path('goToCart/', login_required(views.goToCartListView.as_view()),name="GoToCart"),
    path('increaseqty/', login_required(views.UpdateCartIncreaeQty.as_view()),name="updateIncreaseQty"),
    path('decreaseqty/', login_required(views.UpdateCartDecreaseQty.as_view()),name="updatedecreaseQty"),
    path('cartdel/', login_required(views.DeleteCartDecreaseQty.as_view()),name="deleteCart"),
    path('goToCheckout/', login_required(views.doChckout.as_view()),name="checkout"),
    path('jazzcashResponse/', login_required(views.jazzcashResponse.as_view()),name="jazzcashResponse"),
    path('transcationCustom/', login_required(views.TranscationCustom.as_view()),name="transcationCustome"),
    path('signup/', views.CustomSignupView.as_view(), name='sign_up_custom'),
    # path('login/', views.CustomloginView.as_view(), name='login_custom'),
    # path('logout/' ,LogoutView.as_view(),name='logout_custom'),
    # path('paswordChange/',views.CustomPasswordChangeView.as_view(),name='ChangeCustom_custom'),
    # path('relatedCategory/<int:catid>', views.SelectRelatedCategory,name="productList"),
]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
