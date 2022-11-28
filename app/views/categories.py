
from django.shortcuts import render
from django.http import HttpRequest
from app.models import Category

def index(request):
    assert isinstance(request, HttpRequest)
    Categories = Category.objects.all()
    return render(
        request,
        'app/categories/index.html',
        {
            'Categories' : Categories
        }
    )
    
def create(request):
    form = CategoryForm()
    return render(
        request,
        'app/categories/create.html',
        {
            'form' : form
        }
    )
def store(request):
    if request.method == 'POST':
        form = CategoryForm(request.POST)
        if form.is_valid():
            form.save()
        return redirect('/categories')

def edit(request, id):
    assert isinstance(request, HttpRequest)
    if request.method == "GET":
        if id == 0:
            form = CategoryForm()
        else:
            Category = Category.objects.get(pk=id)
            form = CategoryForm(isinstance=category)
        return render(
            request,
            'app/categories/edit.html',
            {
                'form': form
            } 
        ) 
    else:
        if id == 0:
            form = CategoryForm(request.POST)
        else:
            Category = Category.objects.get(pk=id)
            form = CategoryForm(request.POST,isinstance=category)
        if form.is_valid():
            form.save()
        return redirect('/categories') 
    delete(request, id)
    Category = Category.objects.get(pk=id)
    Category.delete
    returnredirect('/categories')
def delete(request, id):
    Categories = Category.objects.get(pk=id)
    Categories.delete
    messages.success(request,"suppression de la categorie avec success")
    return redirect('/categories')   

def edit_insert(request, id):
    assert isinstance(request, HttpRequest)
    if request.method == "GET":
        if id == 0:
            form = CategoryForm()
        else:
            Categories = Category.objects.get(pk=id)
            form = CategoryForm(isinstance=Categories)
        return render(
            request, 
            'app/categories/edit.html',
           
            {
                'form': form
            }  
        )
    else:
        if id == 0:
            form = CategoryForm(request.POST)
        else:    
            Categories = Category.objects.get(pk=id)
            form = CategoryForm(request.POST,isinstance=Categories)
        if form.is_valid():
            form.save
            messages.success(request,"modification de la categorie avec success")
            return render('/categories')






