from django.shortcuts import render, get_object_or_404, redirect
from .models import Product
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User

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

@login_required(login_url='/login')
def product_create_view(request):
    form = ProductForm(request.POST or None, request.FILES or None)
    if form.is_valid():
        #form.save();
        #form = ProductForm()
        current_form = form.save(commit=False)
        current_form.seller = request.user
        current_form.save()
        return redirect('/')

    context = {
        'form': form
    }
    return render(request, "products/product_create.html", context)

@login_required(login_url='/login')
def product_update_view(request, id=id):
    obj = get_object_or_404(Product, id=id)
    if not obj.seller == request.user:
        return redirect('../')
    form = ProductForm(request.POST or None, request.FILES or None, instance=obj)
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

@login_required(login_url='/login')
def product_delete_view(request, id):
    obj = get_object_or_404(Product, id=id)
    if not obj.seller == request.user:
        return redirect('../')
    if request.method == "POST":
        obj.delete()
        return redirect('')
    context = {
        "object":obj
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
