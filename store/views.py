from django.shortcuts import render
from django.views import generic

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
