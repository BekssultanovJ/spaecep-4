from django.urls import path

from order.views import AddToCartView, RemoveFromCartView, CartDetailsView

urlpatterns = [
    path('add/<int:product_id>/', AddToCartView.as_view(), name='add-to-cart'),
    path('remove/<int:product_id>/', RemoveFromCartView.as_view(), name='remove-from-cart'),
    path('',CartDetailsView.as_view(), name='cart-details'),
    # path('increment/<int:product_id>/', IncrmentQuantityView.as_view(), name='increment_quantity')
]