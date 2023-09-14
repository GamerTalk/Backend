from django.test import TestCase
from .models import Users, Genre

# Create your tests here.

class UsersModelTest(TestCase):
    def test_user_model_exist(self):
        users = Users.objects.count()

        self.assertEqual(users, 0)

    def test_model_has_string_representation(self):
        user = Users.objects.create(
            uid="q5lS9Ac17hM1fXXmr8ZpFghvz7W2",
            username="GodSlayerXD",
            date_of_birth="1999-01-01",
            about_me="I was born in a log cabin.",
            languages={
                "fluent": ["english", "spanish"],
                "learning": [
                    {"level": 1, "language": "german"},
                    {"level": 3, "language": "japanese"},
                ],
            },
            currently_playing="I am currently playing COD MW2, Fortnite, and some Ark Survival",
            user_systems=["pc", "playstation"],
            user_genre=["survival", "shooters"],
            user_region="north america",
        )

        self.assertEqual(str(user), user.uid)
