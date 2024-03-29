from django.urls import path
from .views import (
    # HomeView,
    CatHomeView,
    OrderSummaryView,
    # CheckoutView,
    ItemDetailView,
    # add_to_cart,
    # remove_from_cart,
    # remove_single_item_from_cart,
    # AddCouponView
)

app_name = 'core'

urlpatterns = [
    path('', CatHomeView,name='cat-home' ,kwargs={'cat':'0'}),
    path('<cat>/', CatHomeView,name='cat-home'),
    # path('checkout/',CheckoutView.as_view(), name='checkout'),
    path('order-summary/', OrderSummaryView.as_view(),name='order-summary'),
    path('product/<pk>/', ItemDetailView.as_view() ,name='product'),
    # path('add-to-cart/<slug>/', add_to_cart, name='add-to-cart'),
    # path('add-coupon/', AddCouponView.as_view(), name='add-coupon'),
    # path('remove-from-cart/<slug>/', remove_from_cart, name='remove-from-cart'),
    # path('remove-single-item-from-cart/<slug>/', remove_single_item_from_cart, name='remove-single-item-from-cart'),
    # # path('payment/<payment_option>/', PaymentView.as_view(), name='payment'),
    # # path('request-refund/', RequestRefundView.as_view(), name='request-refund')
]