from django.views.generic.list import ListView

from .models import Product
from django.db import models


class Index(ListView):
    model = Product
    template_name = 'catalog/index.html'
    context_object_name = 'products'


    def get_queryset(self, *, object_list=None, **kwargs):
        products = []
        for j in Product.objects.all():

            if len(j.description) > 100:
                j.description = j.description[:101]
            products.append(j)
        return products
