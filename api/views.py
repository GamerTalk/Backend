from rest_framework.response import Response
from rest_framework.decorators import api_view
from base.models import (
    Users,
    english,
    spanish,
    french,
    german,
    japanese,
    chinese,
    korean,
    systems,
    genre,
    messages,
)
from .serializers import (
    UsersSerializer,
    englishSerializer,
    spanishSerializer,
    frenchSerializer,
    germanSerializer,
    japaneseSerializer,
    chineseSerializer,
    koreanSerializer,
    systemsSerializer,
    genraSerializer,
    messagesSerializer,
)
import json


@api_view(["GET"])
def hello(request):
    return Response({"hello": "world"})


@api_view(["GET"])
def testhello(request):
    test = ["Jack Johnson", "John Jackson"]
    return Response(test)


@api_view(["POST"])
def NewUser(request):
    uid = request.data["uid"]
    username = request.data["username"]
    about_me = request.data["about_me"]
    fluent = request.data["fluent"]
    learning = request.data["learning"]
    date_of_birth = request.data["date_of_birth"]
    user_systems = request.data["systems"]
    genre = request.data["genre"]
    languages_column = {"fluent": fluent, "learning": learning}

# structures the data how the Users table wants it
    users_data = {
        "uid": uid,
        "username": username,
        "date_of_birth": date_of_birth,
        "about_me": about_me,
        "languages": languages_column
    }

# added the user to the Users table
    user_serializer = UsersSerializer(data=users_data)
    if user_serializer.is_valid():
        user_serializer.save()
    else:
            errors = user_serializer.errors
            return Response({'errors': errors}, status=400)

    model_map = {
        'english': (english, englishSerializer),
        'spanish': (spanish, spanishSerializer),
        'german': (german, germanSerializer),
        'french': (french, frenchSerializer),
        'japanese': (japanese, japaneseSerializer),
        'chinese': (chinese, chineseSerializer),
        'korean': (korean, koreanSerializer),
    }

# adds the languages the user is fluent in to the appropriate language tables
    # for item in fluent:
    #     language = item.lower()
    #     if language in model_map:
    #         ModelClass, SerializerClass = model_map[language]
    #         data = {
    #             "user_uid": uid,
    #             "level": 4
    #         }
    #         serializer = SerializerClass(data=data)
    #         if serializer.is_valid():
    #             serializer.save()


    return Response(
        {
            "uid": uid,
            "username": username,
            "about_me": about_me,
            "fluent": fluent,
            "learning": learning,
            "date_of_birth": date_of_birth,
            "languages_column": languages_column,
            "systems": user_systems,
            "genre": genre
        }
    )
