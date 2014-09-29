"""integration tests for blog app"""

from django.contrib.auth import get_user_model
from django.core.exceptions import ObjectDoesNotExist
from django.test import Client, TestCase

from portal.fixtures import USERS

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

    @classmethod
    def setUpClass(cls):
        """prepare test environment"""

        # setup fixtures
        cls.create_users()


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
