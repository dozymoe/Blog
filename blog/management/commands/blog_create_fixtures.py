from copy import copy
from django.contrib.auth import get_user_model
from django.core.exceptions import ObjectDoesNotExist
from django.core.management.base import BaseCommand

from blog.models import Category, Post
from blog.fixtures import CATEGORIES, POSTS

class Command(BaseCommand):
    def handle(self, *args, **options):
        # get available user
        user = get_user_model().objects.get(id=1)

        # create categories from fixture
        for c in CATEGORIES:
            try:
                Category.objects.get(name=c['name'])
                continue
            except ObjectDoesNotExist:
                pass
            Category.objects.create(**c)

        # create posts from fixture
        for post in POSTS:
            try:
                Post.objects.get(slug=post['slug'])
                continue
            except ObjectDoesNotExist:
                pass
            p = copy(post)
            c = p.pop('category', None)
            if c:
                c = Category.objects.get(name=c)
            p['category'] = c
            p['author'] = user
            Post.objects.create(**p)
