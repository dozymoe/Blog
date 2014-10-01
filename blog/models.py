"""database definition for Post and Category model"""

from django.contrib.auth.models import User
from django.db import models
from django.utils.text import slugify
from taggit.managers import TaggableManager


class Category(models.Model):
    """data definition for blog post's category"""

    name = models.CharField(max_length=30, unique=True)
    is_active = models.BooleanField(default=True)

    class Meta(object):
        verbose_name_plural = 'Categories'

    def __unicode__(self):
        return self.name

    @staticmethod
    def fixtures():
        """get fixture to be used in tests"""
        from .fixtures import CATEGORIES
        return CATEGORIES


class Post(models.Model):
    """data definition for a blog post"""

    title = models.CharField(max_length=200)
    slug = models.SlugField(max_length=200, unique=True)
    category = models.ForeignKey(Category, related_name='posts')
    description = models.CharField(max_length=220)
    content = models.TextField()
    publish = models.BooleanField(default=True)
    author = models.ForeignKey(User, related_name='posts')
    created = models.DateTimeField(auto_now_add=True)
    tags = TaggableManager(blank=True)

    def __unicode__(self):
        return self.title

    def save(self, force_insert=False, force_update=False, using=None,
             update_fields=None):
        if not getattr(self, 'slug'):
            self.slug = slugify(self.title)
        super(Post, self).save(force_insert=force_insert, force_update=force_update,
                               using=using, update_fields=update_fields)

    @staticmethod
    def fixtures():
        """get fixture to be used in tests"""
        from .fixtures import POSTS
        return POSTS
