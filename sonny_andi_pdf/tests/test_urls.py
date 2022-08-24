from django.test import SimpleTestCase
from django.test import Client

from django.urls import reverse, resolve
from sonny_andi_pdf.views import prototype
from rest_framework import status


class TestUrls(SimpleTestCase):

    def test_prototype_url_is_resolved(self):
        client = Client()
        url = reverse('prototype')
        response = client.get(url, data=None)
        self.assertEquals(response.status_code, status.HTTP_200_OK)

