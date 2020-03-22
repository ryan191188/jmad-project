from django.test import TestCase
from django.urls import resolve

from solos.views import index


class SolosUrlsTestCase(TestCase):

    def test_root_url_uses_index_view(self):
        """
        Test that the root of the sites resolves to the
        correct view function
        """
        root = resolve('/')
        self.assertEqual(root.func, index)
