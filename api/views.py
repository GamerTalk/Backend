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

@api_view(["GET"])
def allUsers(request):
    allUsers = Users.objects.all()
    serializer = UsersSerializer(allUsers, many=True)
    return Response(serializer.data)

@api_view(["GET"])
def filterUsers(request):
    user_agent = request.headers
    genre = user_agent.get("genre")
    print(genre)
    return Response(user_agent)


@api_view(["POST"])
def NewUser(request):

# sample body
# {
#     "uid": "delete me",
#     "username": "GodSlayerXD",
#     "about_me": "I was born in a log cabin.",
#     "fluent": ["english", "spanish"],
#     "learning": [{"language":"german", "level": 1}, {"language":"japanese", "level": 3}],
#     "date_of_birth": "1999-01-01",
#     "systems": ["playstation","PC"],
#     "genre": ["FPS", "survival"],
#     "currently_playing": "I am currently playing COD MW2, Fortnite, and some Ark Survival"
# }
    uid = request.data["uid"]
    username = request.data["username"]
    about_me = request.data["about_me"]
    fluent = request.data["fluent"]
    learning = request.data["learning"]
    date_of_birth = request.data["date_of_birth"]
    user_systems = request.data["systems"]
    genre = request.data["genre"]
    currently_playing = request.data["currently_playing"]
    languages_column = {"fluent": fluent, "learning": learning}

# structures the data how the Users table wants the payload
    users_data = {
        "uid": uid,
        "username": username,
        "date_of_birth": date_of_birth,
        "about_me": about_me,
        "languages": languages_column,
        "currently_playing": currently_playing
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
    for item in fluent:
        language = item.lower()
        if language in model_map:
            ModelClass, SerializerClass = model_map[language]
            payload = {
                "user_uid": uid,
                "level": 4
            }
            serializer = SerializerClass(data=payload)
            if serializer.is_valid():
                serializer.save()
            else:
                errors = serializer.errors
                return Response({'errors': errors}, status=400)

# adds the languages the user is learning in to the appropriate language tables
    for item in learning:
        language = item["language"].lower()
        level = item["level"]
        if language in model_map:
            ModelClass, SerializerClass = model_map[language]
            payload = {
                "user_uid": uid,
                "level": level
            }
            serializer = SerializerClass(data=payload)
            if serializer.is_valid():
                serializer.save()
            else:
                errors = serializer.errors
                return Response({'errors': errors}, status=400)
            
# adds the system the user plays on to the systems table
    for system in user_systems:
        payload = {
            "user_uid": uid,
            "system": system
        }
        serializer = systemsSerializer(data=payload)
        if serializer.is_valid():
            serializer.save()
        else:
            errors = serializer.errors
            return Response({'errors': errors}, status=400)
            
# adds the genre the user plays on to the genre table
    for single_genre in genre:
        payload = {
            "user_uid": uid,
            "genre": single_genre
        }
        serializer = genraSerializer(data=payload)
        if serializer.is_valid():
            serializer.save()
        else:
            errors = serializer.errors
            return Response({'errors': errors}, status=400)


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

