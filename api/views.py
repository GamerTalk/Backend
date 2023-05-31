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

    languages_column = {"fluent": fluent, "learning": learning}

    return Response(
        {
            "uid": uid,
            "username": username,
            "about_me": about_me,
            "fluent": fluent,
            "learning": learning,
            "date_of_birth": date_of_birth,
            "languages_column": languages_column,
        }
    )
