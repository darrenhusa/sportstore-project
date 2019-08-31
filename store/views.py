from django.shortcuts import render
from django.views import generic
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy

from store.models import Product

# Create your views here.

def index(request):
    """View function for home page of site."""

    products = Product.objects.all()
    num_products = Product.objects.all().count()

    context = {
        'products': products,
        'num_products': num_products,
    }

    # Render the HTML template index.html with the data in the context variable
    return render(request, 'index.html', context=context)


class ProductListView(generic.ListView):
    model = Product

class ProductDetailView(generic.DetailView):
    model = Product

class ProductCreate(CreateView):
    model = Product
    fields = '__all__'
    # initial = {'date_of_death': '05/01/2018'}

class ProductUpdate(UpdateView):
    model = Product
    fields = '__all__'
    # fields = ['first_name', 'last_name', 'date_of_birth', 'date_of_death']

class ProductDelete(DeleteView):
    model = Product
    success_url = reverse_lazy('products')
