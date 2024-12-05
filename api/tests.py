from django.test import TestCase
from rest_framework.test import APITestCase
from rest_framework import status
from django.urls import reverse
from rest_framework.test import APIClient
from django.conf import settings
from .views import ExternallRequest, TestRequest
from requests import request as req


class ExternalRequestTests(APITestCase):
    def setUp(self):
        self.client = APIClient()
        self.url = "http://127.0.0.1:8000/" + settings.EXTERNAL_API_URL
        self.method = settings.EXTERNAL_API_METHOD

    def test_external_request(self):
        self.response = req(self.method, self.url)
        self.assertEqual(self.response.status_code, status.HTTP_200_OK)


# Create your tests here.
