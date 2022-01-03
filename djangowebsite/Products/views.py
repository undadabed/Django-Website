from django.shortcuts import render, get_object_or_404, redirect
from .models import Product

from .forms import ProductForm

# Create your views here.
#def product_create_view(request):
#    my_form = RawProductForm()
#    if (request.method == "POST"):
#        my_form = RawProductForm(request.POST)
#        if my_form.is_valid():
#            Product.objects.create(**my_form.cleaned_data)
#    context = {
#        "form": my_form
#    }
#    return render(request, "products/product_create.html", context)

def product_create_view(request):
    form = ProductForm(request.POST or None)
    if form.is_valid():
        form.save();
        form = ProductForm()

    context = {
        'form': form
    }
    return render(request, "products/product_create.html", context)

def product_update_view(request, id=id):
    obj = get_object_or_404(Product, id=id)
    form = ProductForm(request.POST or None, instance=obj)
    if form.is_valid():
        form.save()
    context = {
        'form': form
    }
    return render(request, "products/product_create.html", context)

def product_detail_view(request, id):
    obj = get_object_or_404(Product, id=id)
    context = {
        "object": obj
    }
    return render(request, "products/product_detail.html", context)

def product_delete_view(request, id):
    obj = get_object_or_404(Product, id=id)
    if request.method == "POST":
        obj.delete()
        return redirect('../../')
    context = {
        "ojbect":obj
    }
    return render(request, "products/product_delete.html", context)

def product_list_view(request):
    queryset = Product.objects.all()
    context = {
        "object_list": queryset
    }
    return render(request, "products/products_list.html", context)

def cart_view(request):
    return
