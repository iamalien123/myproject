from django.urls import path
from . import views

app_name = 'shop'  # Define the namespace

urlpatterns = [
    path('', views.product_list, name='product_list'),
    path('category/<slug:category_slug>/', views.product_list, name='product_list_by_category'),
    path('product/<int:product_id>/', views.product_detail, name='product_detail'),
    path('cart/', views.cart_detail, name='cart_detail'),
    path('cart/add/<int:product_id>/', views.add_to_cart,name='add_to_cart'),
    path('register/', views.register, name='register'),  # Add this line
    path('login/', views.user_login, name='login'),     # Add this line
]