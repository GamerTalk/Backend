from django.db.models import Q
from django.core import serializers
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
    region,
    posts,
    flashcards
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
    regionSerializer,
    postsSerializer,
    flashCardsSerialized
)
import json
import os
import dotenv

dotenv.load_dotenv()

SECRET_CODE = os.getenv("SECRET_CODE")

model_map = {
    'english': (english, englishSerializer),
    'spanish': (spanish, spanishSerializer),
    'german': (german, germanSerializer),
    'french': (french, frenchSerializer),
    'japanese': (japanese, japaneseSerializer),
    'chinese': (chinese, chineseSerializer),
    'korean': (korean, koreanSerializer),
}


@api_view(["GET"])
def hello(request):
    return Response({"hello": "world"})


@api_view(["GET"])
def testhello(request):
    test = ["Jack Johnson", "John Jackson"]
    return Response(test)

# @api_view(["GET"])
# def allUsers(request):
#     allUsers = Users.objects.all()
#     serializer = UsersSerializer(allUsers, many=True)
#     return Response(serializer.data)

@api_view(["GET"])
def userInfo(request):
    user_agent = request.headers
    uid = user_agent.get("uid")
    singleuser = Users.objects.filter(uid=uid).first()
    serializer = UsersSerializer(singleuser, many=False)
    return Response(serializer.data)

@api_view(["GET"])
def filterUsers(request):

#     sample of what the header must look like (probably an object format with axios)
    # {
    #     systems:["playstation", "switch"]
    #     genre:["shooters", "rpg"]
    #     language: japanese
    #     regions: ["north america"] 
    # }
    user_agent = request.headers
    genre = user_agent.get("genre")
    systems = user_agent.get("systems")
    language = user_agent.get("language")
    regions = user_agent.get("regions")

    search_query = {}

    if genre:
        search_query["genre"] = json.loads(genre)

    if systems:
        search_query["systems"] = json.loads(systems)
    try:
        if language:
            search_query["language"] = language
            print(search_query["language"])
    except TypeError:
        # Do nothing
        x = 1

    if regions:
        search_query["regions"] = json.loads(regions)

    genre_conditions = Q()
    for genre in search_query.get("genre", []):
        genre_conditions |= Q(genre__genre=genre)

    system_conditions = Q()
    for system in search_query.get("systems", []):
        system_conditions |= Q(systems__system=system)
                
    region_conditions = Q()
    for region in search_query.get("regions", []):
        region_conditions |= Q(region__region=region)
                

    results = Users.objects.filter(genre_conditions, system_conditions, region_conditions)
    serialized_results = json.loads(serializers.serialize('json', results))
    # serialized_results = serializers.serialize('json', results, fields=('uid','username', 'genre__genre'))

    # remove duplicate result
    filtered_serialized_results = []
    userLookup = {}

    for user in serialized_results:
        try:
            if userLookup[user["fields"]["uid"]]:
                z=1
        except KeyError:
            filtered_serialized_results.append(user)
            userLookup[user["fields"]["uid"]] = True


    #test that the user speaks the target language
    try:
        if search_query["language"]:
            sendUsers = []
            for user in filtered_serialized_results:
                if search_query["language"] in user["fields"]["languages"]["fluent"]:
                    sendUsers.append(user['fields'])
            # print('🍟🍒😂',sendUsers)
            return Response(sendUsers)
    except KeyError:
        def removeFields(x):
            return x['fields']
        return Response(map(removeFields, filtered_serialized_results))



    # print(search_query)
    # return Response(search_query)


@api_view(["GET"])
def UserFlashcards(request):
    # card_id = user_agent.get("card_id")
    user_agent = request.headers
    user_uid = user_agent.get("uid")

    user_cards_query = flashcards.objects.filter(Q(user_uid=user_uid)).order_by('-id')
    user_cards = flashCardsSerialized(user_cards_query, many=True)

    return Response(user_cards.data)

@api_view(["POST"])
def NewFlashcard(request):
    # Sample body
    # {
    #     "user_uid": "TESTUSER2",
    #     "front":"strength",
    #     "back": "力（ちから）" 
    # }
    user_uid = request.data["user_uid"]
    front = request.data["front"]
    back = request.data["back"]

    new_flashcard_payload = {
        'user_uid': user_uid,
        'front': front,
        'back': back
    }

    new_flashcard_serializer = flashCardsSerialized(data=new_flashcard_payload)

    if new_flashcard_serializer.is_valid():
        new_flashcard_serializer.save()
    else:
        errors = new_flashcard_serializer.errors
        return Response({'errors': errors}, status=400)

    return Response(new_flashcard_payload)

@api_view(["DELETE"])
def DeleteFlashcard(request):
    #sample body
    # card_id will be the id number of the card you want to delete 
    # {
    # "user_uid": "TESTUSER2",
    # "card_id": 2
    # }
    user_uid = request.data["user_uid"]
    card_id = request.data["card_id"]
    flashcards.objects.filter(Q(user_uid=user_uid) & Q(id=card_id)).delete()

    return Response(True)

@api_view(["POST"])
def NewPost(request):

    #sample body
    # time of message uses ISO formate of javascript date
    # https://www.w3schools.com/js/js_date_formats.asp
    # {
    #     "uid": "TESTUSER2",
    #     "message":"Hello everyone",
    #     "time_of_message": "2015-03-25T12:00:00Z" 
    # }
    uid = request.data["uid"]
    message = request.data["message"]
    time_of_message = request.data["time_of_message"]

    new_post_payload = {
        'sender': uid,
        'time_of_message': time_of_message,
        'message': message
    }

    new_post_serializer = postsSerializer(data=new_post_payload)

    if new_post_serializer.is_valid():
        new_post_serializer.save()
    else:
        errors = new_post_serializer.errors
        return Response({'errors': errors}, status=400)

    return Response(new_post_payload)

@api_view(["GET"])
def GetPosts(request):

    all_posts_query = posts.objects.select_related('sender').order_by('-id').all()
    all_posts = postsSerializer(all_posts_query, many=True)
    return Response(all_posts.data)

@api_view(["POST"])
def NewUser(request):
    # sample body
    # {
    #     "uid": "TESTUSER5",
    #     "username": "TESTUSER5",
    #     "about_me": "I was born in a log cabin.",
    #     "fluent": ["english", "spanish"],
    #     "learning": [{"language":"german", "level": 1}, {"language":"japanese", "level": 3}],
    #     "date_of_birth": "1999-01-01",
    #     "systems": ["playstation","pc"],
    #     "genre": ["shooters", "survival"],
    #     "currently_playing": "I am currently playing COD MW2, Fortnite, and some Ark Survival",
    #     "region": "north america"
    #     "profile_picture_url": urlstring
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
    region = request.data["region"]
    profile_picture_url = request.data["profile_picture_url"]
    languages_column = {"fluent": fluent, "learning": learning}

    # structures the data how the Users table wants the payload
    users_data = {
        "uid": uid,
        "username": username,
        "date_of_birth": date_of_birth,
        "about_me": about_me,
        "languages": languages_column,
        "currently_playing": currently_playing,
        "user_systems": user_systems,
        "user_genre": genre,
        "user_region": region,
        "profile_picture_url": profile_picture_url,
    }

    # added the user to the Users table
    user_serializer = UsersSerializer(data=users_data)
    if user_serializer.is_valid():
        user_serializer.save()
    else:
        errors = user_serializer.errors
        return Response({'errors': errors}, status=400)


    # adds the languages the user is fluent in to the appropriate language tables
    for item in fluent:
        language = item.lower()
        if language in model_map:
            ModelClass, SerializerClass = model_map[language]
            payload = {
                "user_uid": uid,
                "level": 6
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
        
    region_payload = {
        "user_uid": uid,
        "region": region
    }
    region_serializer = regionSerializer(data=region_payload)
    if region_serializer.is_valid():
        region_serializer.save()
    else:
        errors = region_serializer.errors
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
            "genre": genre,
            "region": region
        }
    )

@api_view(["PATCH"])
def EditUser(request):
    # sample body
    # {
    #     "uid": "TESTUSER5",
    #     "username": "TESTUSER5",
    #     "about_me": "I was born in a log cabin.",
    #     "fluent": ["english", "spanish"],
    #     "learning": [{"language":"german", "level": 2}, {"language":"japanese", "level": 3}],
    #     "date_of_birth": "1999-01-01",
    #     "systems": ["playstation","pc"],
    #     "genre": ["shooters", "survival", "fighting"],
    #     "currently_playing": "I am currently playing COD MW2, Fortnite, and some Ark Survival",
    #     "region": "north america",
    #     "profile_picture_url": urlstring
    # }

    uid = request.data["uid"]
    username = request.data["username"]
    about_me = request.data["about_me"]
    fluent = request.data["fluent"]
    learning = request.data["learning"]
    date_of_birth = request.data["date_of_birth"]
    user_systems = request.data["systems"]
    user_genre = request.data["genre"]
    currently_playing = request.data["currently_playing"]
    user_region = request.data["region"]
    profile_picture_url = request.data["profile_picture_url"]
    languages_column = {"fluent": fluent, "learning": learning}

    # Delete old data from all other tables
    english.objects.filter(user_uid=uid).delete()
    spanish.objects.filter(user_uid=uid).delete()
    german.objects.filter(user_uid=uid).delete()
    french.objects.filter(user_uid=uid).delete()
    chinese.objects.filter(user_uid=uid).delete()
    japanese.objects.filter(user_uid=uid).delete()
    korean.objects.filter(user_uid=uid).delete()
    systems.objects.filter(user_uid=uid).delete()
    genre.objects.filter(user_uid=uid).delete()
    region.objects.filter(user_uid=uid).delete()

    # structures the data how the Users table wants the payload
    users_data = {
        "uid": uid,
        "username": username,
        "date_of_birth": date_of_birth,
        "about_me": about_me,
        "languages": languages_column,
        "currently_playing": currently_playing,
        "user_systems": user_systems,
        "user_genre": user_genre,
        "user_region": user_region,
    }

    # added the user to the Users table
    try:
        user_entry = Users.objects.get(uid=uid)
    except Users.DoesNotExist:
        return Response("User does not exist")

    user_entry.about_me = about_me
    user_entry.languages = languages_column
    user_entry.currently_playing = currently_playing
    user_entry.user_systems = user_systems
    user_entry.user_genre = user_genre
    user_entry.user_region = user_region
    user_entry.profile_picture_url = profile_picture_url
    user_entry.save()
    serializer = UsersSerializer(user_entry)

    # adds the languages the user is fluent in to the appropriate language tables
    for item in fluent:
        language = item.lower()
        if language in model_map:
            ModelClass, SerializerClass = model_map[language]
            payload = {
                "user_uid": uid,
                "level": 6
            }
            fluent_serializer = SerializerClass(data=payload)
            if fluent_serializer.is_valid():
                fluent_serializer.save()
            else:
                errors = fluent_serializer.errors
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
            learning_serializer = SerializerClass(data=payload)
            if learning_serializer.is_valid():
                learning_serializer.save()
            else:
                errors = learning_serializer.errors
                return Response({'errors': errors}, status=400)
            
    # adds the system the user plays on to the systems table
    for system in user_systems:
        payload = {
            "user_uid": uid,
            "system": system
        }
        system_serializer = systemsSerializer(data=payload)
        if system_serializer.is_valid():
            system_serializer.save()
        else:
            errors = system_serializer.errors
            return Response({'errors': errors}, status=400)
            
    # adds the genre the user plays on to the genre table
    for single_genre in user_genre:
        payload = {
            "user_uid": uid,
            "genre": single_genre
        }
        genre_serializer = genraSerializer(data=payload)
        if genre_serializer.is_valid():
            genre_serializer.save()
        else:
            errors = genre_serializer.errors
            return Response({'errors': errors}, status=400)
        
    region_payload = {
        "user_uid": uid,
        "region": user_region
    }
    region_serializer = regionSerializer(data=region_payload)
    if region_serializer.is_valid():
        region_serializer.save()
    else:
        errors = region_serializer.errors
        return Response({'errors': errors}, status=400)


    return Response(serializer.data)

@api_view(["DELETE"])
def deleteUser(request):
    # Sample body
    # {
    #     "uid": "user uid",
    #     "secretCode": "unique code"
    # }
    uid = request.data["uid"]

    if request.data["secretCode"] == SECRET_CODE:
        try:
            Users.objects.filter(uid=uid).delete()
            return Response("Success")
        except Users.DoesNotExist:
            return Response("User does not exist")
    else:
        return Response("Need verification code")
