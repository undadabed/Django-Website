from django.urls import path
from .views import product_detail_view, product_create_view, product_delete_view, product_list_view, product_update_view, product_purchase_view, cart_view, seller_view

app_name = 'products'
urlpatterns = [
    path('', product_list_view, name='product-list'),
    path('cart/', cart_view, name='cart'),
    path('orders/', seller_view, name='orders'),
    path('create/', product_create_view, name='product-create'),
    path('<int:id>/', product_detail_view, name='product-detail'),
    path('<int:id>/delete/', product_delete_view, name='product-delete'),
    path('<int:id>/update/', product_update_view, name='product-update'),
    path('<int:id>/purchase/', product_purchase_view, name='product-purchase'),
]