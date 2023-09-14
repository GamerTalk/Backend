from rest_framework import serializers
from base.models import Users, English, Spanish, French, German, Japanese, Chinese, Korean, Systems, Genre, Messages, Region, Posts, Flashcards


class UsersSerializer(serializers.ModelSerializer):
    class Meta:
        model = Users
        fields = '__all__'

class EnglishSerializer(serializers.ModelSerializer):
    class Meta:
        model = English
        fields = '__all__'

class SpanishSerializer(serializers.ModelSerializer):
    class Meta:
        model = Spanish
        fields = '__all__'

class FrenchSerializer(serializers.ModelSerializer):
    class Meta:
        model = French
        fields = '__all__'

class GermanSerializer(serializers.ModelSerializer):
    class Meta:
        model = German
        fields = '__all__'

class JapaneseSerializer(serializers.ModelSerializer):
    class Meta:
        model = Japanese
        fields = '__all__'

class ChineseSerializer(serializers.ModelSerializer):
    class Meta:
        model = Chinese
        fields = '__all__'

class KoreanSerializer(serializers.ModelSerializer):
    class Meta:
        model = Korean
        fields = '__all__'

class SystemsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Systems
        fields = '__all__'

class GenreSerializer(serializers.ModelSerializer):
    class Meta:
        model = Genre
        fields = '__all__'

class MessagesSerializer(serializers.ModelSerializer):
    class Meta:
        model = Messages
        fields = '__all__'

class RegionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Region
        fields = '__all__'

class PostsSerializer(serializers.ModelSerializer):
    sender_uid = serializers.CharField(source='sender.uid', max_length=100, read_only=True)
    sender_data = serializers.SerializerMethodField()

    class Meta:
        model = Posts
        fields = '__all__'

    def get_sender_data(self, instance):
        sender_uid = instance.sender.uid
        try:
            sender = Users.objects.get(uid=sender_uid)
            sender_serializer = UsersSerializer(sender)
            return sender_serializer.data
        except Users.DoesNotExist:
            return {}

    def create(self, validated_data):
        sender_uid = validated_data.pop('sender')

        try:
            sender = Users.objects.get(uid=sender_uid)
        except Users.DoesNotExist:
            raise serializers.ValidationError("Invalid sender UID")

        validated_data['sender'] = sender
        post = Posts.objects.create(**validated_data)

        return post
    
class FlashCardsSerialized(serializers.ModelSerializer):
    class Meta:
        model = Flashcards
        fields = '__all__'