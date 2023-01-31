from django.forms import *
from django.views.generic import ListView, CreateView
from .forms import *
from .models import *
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


class VersionCreate(CreateView):
    model = Version
    form_class = VersionForm
    template_name = 'catalog/version_form.html'


    def get_context_data(self, **kwargs):
        context_data = super().get_context_data(**kwargs)

        Formset = inlineformset_factory(Product, self.model, form=VersionForm, extra=1)

        if self.request.method == 'POST':
            formset = Formset(self.request.POST, instance=self.object)
        else:
            formset = Formset(instance=self.object)

        context_data['formset'] = formset
        return context_data


    def form_valid(self, form):
        context_data = self.get_context_data()
        formset = context_data['formset']
        with transaction.atomic():
            if form.is_valid():
                self.object = form.save()
                if formset.is_valid():
                    formset.instance = self.object
                    formset.save()

        return super().form_valid(form)
