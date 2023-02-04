from django.db import models
from autoslug import AutoSlugField
from django.urls import reverse

from users.models import User


class BlogMain(models.Model):
    title = models.CharField('Заголовок', max_length=255)
    slug = AutoSlugField(populate_from='title', unique=True)
    content = models.TextField(blank=True)
    image = models.ImageField(upload_to='photos/%Y/%m/%d', blank=True)
    create_date = models.DateTimeField(auto_now_add=True)
    is_public = models.BooleanField(default=True)
    views_count = models.IntegerField(default=0)
    _user = models.ForeignKey(User, default=None, null=True, on_delete=models.CASCADE)


    class Meta:
        verbose_name = 'Blog'
        verbose_name_plural = 'Blogs'


    def get_absolute_url(self):
        return reverse('blog:read', kwargs={'slug': self.slug})


    def __str__(self):
        return self.title
