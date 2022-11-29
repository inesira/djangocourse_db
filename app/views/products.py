from django.shortcuts import redirect,render
from django.http import HttpRequest
from app.models import Product
from app.forms import ProductForm
from django.contrib import messages

def index(request):
    assert isinstance(request, HttpRequest)
    Products = Products.objects.all()
    return render(
        request,
        'app/products/index.html',
        {
            'Products' : Products
        }
    )
    
def create(request):
    form = ProductForm()
    return render(
        request,
        'app/products/create.html',
        {
            'form' : form
        }
    )
def store(request):
    if request.method == 'POST':
        form = ProductForm(request.POST)
        if form.is_valid():
            form.save()
        return redirect('/products')

def edit(request, id):
    assert isinstance(request, HttpRequest)
    if request.method == "GET":
        if id == 0:
            form = ProductForm()
        else:
            products = Product.objects.get(pk=id)
            form = ProductForm(isinstance=products)
        return render(
            request,
            'app/products/edit.html',
            {
                'form': form
            } 
        ) 
    else:
        if id == 0:
            form = ProductForm(request.POST)
        else:
            Products = Products.objects.get(pk=id)
            form = ProductForm(request.POST,isinstance=product)
        if form.is_valid():
            form.save()
        return redirect('/products') 
    delete(request, id)
    Products = Products.objects.get(pk=id)
    Products.delete
    returnredirect('/products')
def delete(request, id):
    Products = Products.objects.get(pk=id)
    Products.delete
    messages.success(request,"suppression de la categorie avec success")
    return redirect('/products')   

def edit_insert(request, id):
    assert isinstance(request, HttpRequest)
    if request.method == "GET":
        if id == 0:
            form = ProductForm()
        else:
            Products = Products.objects.get(pk=id)
            form = ProductForm(isinstance=Products)
        return render(
            request, 
            'app/products/edit.html',
           
            {
                'form': form
            }  
        )
    else:
        if id == 0:
            form = ProductForm(request.POST)
        else:    
            Products = Products.objects.get(pk=id)
            form = ProductForm(request.POST,isinstance=Products)
        if form.is_valid():
            form.save
            messages.success(request,"modification de la categorie avec success")
            return render('/products')






