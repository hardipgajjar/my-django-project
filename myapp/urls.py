from django.urls import path
from . import views

urlpatterns = [
    path('',views.index,name='index'),
    path('contact/',views.contact,name='contact'),
    path('about/',views.about, name='about'),
    path('shop/',views.shop, name='shop'),
    path('cart/',views.cart,name='cart'),
    path('login/',views.login,name='login'),
    path('signup/',views.signup,name='signup'),
    path('logout/',views.logout,name='logout'),
    path('change_password/',views.change_password,name='change_password'),
    path('seller_change_password/',views.seller_change_password,name='seller_change_password'),
    path('seller_add_product/',views.seller_add_product,name='seller_add_product'),
    path('seller_index/',views.seller_index,name='seller_index.html'),
    path('seller_header/',views.seller_header,name='seller_header.html'),
    path('seller_view_product/', views.seller_view_product,name='seller_view_product'),
    path('seller_product_details/<int:pk>/',views.seller_product_details,name='seller_product_details'),
    path('seller_edit_product/<int:pk>/',views.seller_edit_product,name='seller_edit_product'),
    path('seller_delete_product/<int:pk>/',views.seller_delete_product, name='seller_delete_product'),
    path('wishlist/',views.wishlist,name='wishlist'),
    path('add_to_wishlist/<int:pk>/',views.add_to_wishlist,name='add_to_wishlist'),
    path('product_details/<int:pk>/',views.product_details,name='product_details'),
    path('remove_from_wishlist/<int:pk>/',views.remove_from_wishlist,name='remove_from_wishlist'),
    path('add_to_cart/<int:pk>/',views.add_to_cart,name='add_to_cart'),
    path('remove_from_cart/<int:pk>/',views.remove_from_cart,name='remove_from_cart'),
    path('change_qty',views.change_qty,name='change_qty'),
    path('pay/', views.initiate_payment, name='pay'),
    path('callback/', views.callback, name='callback'),
    path('myorders/',views.myorders,name='myorders'),
    path('forgot_password/',views.forgot_password,name='forgot_password'),
    path('varify_otp/',views.varify_otp,name='varify_otp'),
    path('new_password/',views.new_password,name='new_password'),
    path('ajax/validate_email/',views.validate_email,name="/ajax/validate_email/"),

    


]
