"""integration tests for blog app"""

from django.contrib.auth import get_user_model
from django.core.exceptions import ObjectDoesNotExist
from django.core.urlresolvers import reverse
from django.test import Client, TestCase

from portal.fixtures import USERS
from .models import Category, Post

BASE_URL_ADMIN = '/admin/blog/post/'


class TestCaseBase(TestCase):
    """helps create fixtures"""

    maxDiff = None

    @staticmethod
    def create_users():
        """create users from global USERS"""
        for u in USERS:
            user = USERS[u]
            try:
                get_user_model().objects.get(username=user['username'])
            except ObjectDoesNotExist:
                if u == 'superuser':
                    get_user_model().objects.create_superuser(**user)
                else:
                    get_user_model().objects.create_user(**user)

    @staticmethod
    def create_blog_categories():
        """create object from category fixtures"""
        for c in Category.fixtures():
            Category.objects.create(**c)

    @staticmethod
    def create_blog_posts():
        """create objects from post fixtures"""
        user = get_user_model().objects.get(username=USERS['superuser']['username'])
        for p in Post.fixtures():
            c_name = p.pop('category')
            category = Category.objects.get(name=c_name)
            p['author'] = user
            p['category'] = category
            Post.objects.create(**p)

    @classmethod
    def setUpClass(cls):
        """prepare test environment"""

        # setup fixtures
        cls.create_users()
        cls.create_blog_categories()
        cls.create_blog_posts()


class PostAdminView(TestCaseBase):
    """integration tests for Post model"""

    def test_admin_add(self):
        """check django admin add page"""
        c = Client()
        url = BASE_URL_ADMIN + 'add/'

        # test as anonymous
        response = c.get(url)
        self.assertEqual(response.status_code, 302) # this should've been 403

        # test as superuser
        self.assertEqual(c.login(**USERS['superuser']), True)
        response = c.get(url)
        self.assertEqual(response.status_code, 200)

    def test_admin_list_change(self):
        """check django admin list page"""
        c = Client()
        url = BASE_URL_ADMIN

        # test as anonymous
        response = c.get(url)
        self.assertEqual(response.status_code, 302) # this should've been 403

        # test as superuser
        self.assertEqual(c.login(**USERS['superuser']), True)
        response = c.get(url)
        self.assertEqual(response.status_code, 200)


class PostNormalView(TestCase):
    """integration tests for Post model"""

    def test_detail(self):
        """check detail page for Post"""
        c = Client()

        # test as anonymous
        for p in Post.fixtures():
            url = reverse('blog:detail', kwargs={'slug': p['slug']})
            response = c.get(url)
            self.assertEqual(response.status_code, 200)

    def test_index(self):
        """check index page for Post"""
        c = Client()
        url = '/'

        # test as anonymous
        response = c.get(url)
        self.assertEqual(response.status_code, 200)
