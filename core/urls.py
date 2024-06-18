from django.conf import settings
from django.conf.urls.static import static
from django.urls import path
from .views import (
    ItemDetailView,
    CheckoutView,
    HomeView,
    OrderSummaryView,
    add_to_cart,
    remove_from_cart,
    remove_single_item_from_cart,
    search_products,
    PaymentView,
    AddCouponView,
    RequestRefundView
)

app_name = "core"

urlpatterns = [
    path("", HomeView.as_view(), name="home"),
    path('search/', search_products, name='search_products'),
    path("checkout/", CheckoutView.as_view(), name="checkout"),
    path("order-summary/", OrderSummaryView.as_view(), name="order-summary"),
    path("product/<slug>/", ItemDetailView.as_view(), name="product"),
    path("add-to-cart/<slug>/", add_to_cart, name="add-to-cart"),
    path("add-coupon/", AddCouponView.as_view(), name="add-coupon"),
    path("remove-from-cart/<slug>/", remove_from_cart, name="remove-from-cart"),
    path("remove-item-from-cart/<slug>/", remove_single_item_from_cart,
         name="remove-single-item-from-cart"),
    path("payment/<payment_option>/", PaymentView.as_view(), name="payment"),
    path("request-refund/", RequestRefundView.as_view(), name="request-refund")
]

if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
