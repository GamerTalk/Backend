from django.test import TestCase
from .models import Users, English, Spanish, French, German, Japanese, Chinese, Korean, Systems, Genre, Messages, Region, Posts, Flashcards

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

class EnglishModelTest(TestCase):
    def test_english_model_exist(self):
        english = English.objects.count()

        self.assertEqual(english, 0)

class SpanishModelTest(TestCase):
    def test_spanish_model_exist(self):
        spanish = Spanish.objects.count()

        self.assertEqual(spanish, 0)

class FrenchModelTest(TestCase):
    def test_french_model_exist(self):
        french = French.objects.count()

        self.assertEqual(french, 0)

class GermanModelTest(TestCase):
    def test_german_model_exist(self):
        german = German.objects.count()

        self.assertEqual(german, 0)

class JapaneseModelTest(TestCase):
    def test_japanese_model_exist(self):
        japanese = Japanese.objects.count()

        self.assertEqual(japanese, 0)

class ChineseModelTest(TestCase):
    def test_chinese_model_exist(self):
        chinese = Chinese.objects.count()

        self.assertEqual(chinese, 0)

class KoreanModelTest(TestCase):
    def test_korean_model_exist(self):
        korean = Korean.objects.count()

        self.assertEqual(korean, 0)

class SystemsModelTest(TestCase):
    def test_systems_model_exist(self):
        systems = Systems.objects.count()

        self.assertEqual(systems, 0)

class GenreModelTest(TestCase):
    def test_genre_model_exist(self):
        genre = Genre.objects.count()

        self.assertEqual(genre, 0)

class RegionModelTest(TestCase):
    def test_region_model_exist(self):
        region = Region.objects.count()

        self.assertEqual(region, 0)

class MessagesModelTest(TestCase):
    def test_messages_model_exist(self):
        messages = Messages.objects.count()

        self.assertEqual(messages, 0)

class FlashcardsModelTest(TestCase):
    def test_flashcards_model_exist(self):
        flashcards = Flashcards.objects.count()

        self.assertEqual(flashcards, 0)

class PostsModelTest(TestCase):
    def test_posts_model_exist(self):
        posts = Posts.objects.count()

        self.assertEqual(posts, 0)