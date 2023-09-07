from django.test import TestCase
from .models import Users

# Create your tests here.

class UserModelTest(TestCase):
    def test_user_model_exist(self):
        users = Users.objects.count()

        self.assertEqual(users, 0)