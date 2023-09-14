from django.test import TestCase
from base.models import Users
from .serializers import UsersSerializer
import json

class API_endpoint_test(TestCase):
    def test_hello_endpoint(self):
        response = self.client.get("/api/")

        self.assertEqual(response.status_code, 200)

        content = json.loads(response.content.decode("utf-8"))

        self.assertEqual(content, {"hello": "world"})