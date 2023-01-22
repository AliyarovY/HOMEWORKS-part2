from django.contrib import admin

from blog.models import *


@admin.register(BlogMain)
class BlogMainAdmin(admin.ModelAdmin):
    list_display = tuple('title slug image'.split())

