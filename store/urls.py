from django.urls import path
from . import views 

urlpatterns = [
    path('store/', views.store, name="store"),
    path('cart/', views.cart, name="cart"),
    path('checkout/', views.checkout, name="checkout"),
    path('update_item/', views.updateItem, name="update_item"),
    path('process_order/', views.processOrder, name="process_order"),
    path('orders_processed/', views.orders_processed, name="orders_processed"),
    path('order_posted/<int:orderId>', views.order_posted, name="order_posted"),
]