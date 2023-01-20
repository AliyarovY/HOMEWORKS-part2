from django.shortcuts import render
from .models import Product
from django.db import models


def index(request):
    products = []
    for j in Product.objects.all():

        if len(j.description) > 100:
            j.description = j.description[:101]
        products.append(j)

    return render(request, 'catalog/index.html', {'products': products})
