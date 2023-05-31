from rest_framework.response import Response
from rest_framework.decorators import api_view
from base.models import Users, english, spanish, french, german, japanese, chinese, korean, systems, genre, messages
from .serializers import UsersSerializer, englishSerializer, spanishSerializer, frenchSerializer, germanSerializer, japaneseSerializer, chineseSerializer, koreanSerializer, systemsSerializer, genraSerializer, messagesSerializer

@api_view(['GET'])
def hello(request):
    return Response({'hello':'world'})

@api_view(['GET'])
def testhello(request):
    test = ["Jack Johnson", "John Jackson"]
    return Response(test)