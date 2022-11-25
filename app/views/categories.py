
from django.shortcuts import render
from django.http import HttpRequest
from app.models import Category

def index(request):
    assert isinstance(request, HttpRequest())
    Categories = Category.objects.all()
    return render(
        request,
        'app/categories/index.html',
        {
            'Categories' : Categories
        }
    )
    """
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
        if form.ls_valid
"""