from rest_framework.response import Response
from rest_framework.decorators import api_view
#from base.models import
# from .serializers import 

@api_view(['GET'])
def hello(request):
    return Response({'hello':'world'})

@api_view(['GET'])
def testhello(request):
    test = ["Jack Johnson", "John Jackson"]
    return Response(test)