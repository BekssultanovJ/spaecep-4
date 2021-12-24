from django.shortcuts import render, get_object_or_404, redirect

from django.views import View

from order.forms import AddToCartForm
from order.models import Cart
from product.models import Product


class AddToCartView(View):
    def post(self, request, product_id):
        cart = Cart(request)
        product = get_object_or_404(Product, id=product_id)
        form = AddToCartForm(request.POST)
        if form.is_valid():
            data = form.cleaned_data
            quantity = data.get('quantity')
            cart.add(product.id, quantity)
        return redirect(...)


class RemoveFromCartView(View):
    def get(self, request, product_id):
        cart = Cart(request)
        product = get_object_or_404(Product, id=product_id)
        cart.remove(product_id)
        return redirect(...)

class CartDetailsView(View):
    def get(self, request):
        cart = Cart(request)
        return render(request, 'order/cart_details.html', {'cart': cart})

class IncrementQuantityView(View):
    def get(self, request, product_id):