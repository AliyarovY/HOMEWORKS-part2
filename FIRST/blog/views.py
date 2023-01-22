from django.shortcuts import render, get_object_or_404
from django.urls import reverse_lazy, reverse
from django.views.generic import *

from .models import *


class Index(ListView):
    template_name = 'blog/index.html'
    model = BlogMain


class Create(CreateView):
    model = BlogMain
    slug_url_kwarg = 'slug'
    fields = tuple('title content image is_public'.split())
    template_name = 'blog/create.html'
    success_url = reverse_lazy('blog:main')


class Update(UpdateView):
    model = BlogMain
    slug_url_kwarg = 'slug'
    fields = tuple('title content image is_public'.split())
    template_name = 'blog/delete.html'
    success_url = reverse_lazy('blog:read', kwargs={'slug': slug})


class Delete(DeleteView):
    model = BlogMain
    slug_url_kwarg = 'slug'
    template_name = 'blog/update.html'
    success_url = reverse_lazy('blog:main')


# class Read(DetailView):
#     model = BlogMain
#     template_name = 'blog/read.html'

def Read(request, slug):
    obj = get_object_or_404(BlogMain, slug=slug)
    obj.views_count += 1
    cont = dict(object=obj)
    return render(request, 'blog/read.html', cont)


class PublicOnly(ListView):
    template_name = 'blog/public.html'
    model = BlogMain


    def get_queryset(self):
        return BlogMain.objects.filter(is_public=True)
