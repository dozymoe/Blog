from datetime import datetime

from django.contrib.auth.models import User
from django.db import models
from django.template.defaultfilters import slugify


class Category(models.Model):
    name = models.CharField(max_length=30, unique=True)
    is_active = models.BooleanField(default=True)

    class Meta:
        verbose_name_plural = 'Categories'

    def __unicode__(self):
        return self.name


class Post(models.Model):
    title = models.CharField(max_length=200)
    slug = models.CharField(max_length=200, unique=True)
    category = models.ForeignKey(Category, related_name='posts')
    content = models.TextField()
    publish = models.BooleanField(default=True)
    author = models.ForeignKey(User, related_name='posts')
    created = models.DateTimeField(auto_now_add=True)

    def __unicode__(self):
        return self.title

    def save(self):
        super(Post, self).save()
        created_date = datetime.now()
        self.slug = '{0}/{1}/{2}/{3}/{4}'.format(
            created_date.year, created_date.month, created_date.day, self.id, slugify(self.title)
        )
        super(Post, self).save()

