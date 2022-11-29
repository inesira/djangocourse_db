from django.shortcuts import redirect,render
from django.http import HttpRequest
from app.models import Custormer
from app.forms import CustomerForm
from django.contrib import messages

# Create your views here.
def index(request):
    assert isinstance(request, HttpRequest)
    Customers = Custormer.objects.all()
    return render(
        request,
        'app/customers/index.html',
        {
            'Customers': Customers
        }
    )

def create(request):
    form = CustomerForm()
    return render(
        request,
        'app/customers/create.html',
        {
            'form': form
        }
    )

def store(request):
    if request.method == 'POST':
        form = CustomerForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request," Insertion d'un client avec succe ")
        return redirect('/customers')

def edit(request, id):
    assert isinstance(request, HttpRequest)
    if request.method == "GET":
        if id == 0:
            form = CustomerForm()
        else:
            Customers = Custormer.objects.get(pk=id)
            form = CustomerForm(instance=Customers)
        return render(
            request,
            'app/customers/edit.html',
            {
                'form': form
            }
            )
    else:
        if id == 0:
            form = CustomerForm(request.POST)
        else:
            Customers = Custormer.objects.get(pk=id)
            form = CustomerForm(request.POST,instance=Customers)
        if form.is_valid():
            form.save()
            messages.success(request," Modification d'un client avec succe ")
        return redirect('/customers')
def delete(request, id):
    Customers = Custormer.objects.get(pk=id)
    Customers.delete()
    messages.success(request," Suppression d'un client avec succe ")
    return redirect('/customers')