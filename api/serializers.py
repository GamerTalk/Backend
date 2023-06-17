from rest_framework import serializers
from base.models import Users, english, spanish, french, german, japanese, chinese, korean, systems, genre, messages, region, posts, flashcards


class UsersSerializer(serializers.ModelSerializer):
    class Meta:
        model = Users
        fields = '__all__'

class englishSerializer(serializers.ModelSerializer):
    class Meta:
        model = english
        fields = '__all__'

class spanishSerializer(serializers.ModelSerializer):
    class Meta:
        model = spanish
        fields = '__all__'

class frenchSerializer(serializers.ModelSerializer):
    class Meta:
        model = french
        fields = '__all__'

class germanSerializer(serializers.ModelSerializer):
    class Meta:
        model = german
        fields = '__all__'

class japaneseSerializer(serializers.ModelSerializer):
    class Meta:
        model = japanese
        fields = '__all__'

class chineseSerializer(serializers.ModelSerializer):
    class Meta:
        model = chinese
        fields = '__all__'

class koreanSerializer(serializers.ModelSerializer):
    class Meta:
        model = korean
        fields = '__all__'

class systemsSerializer(serializers.ModelSerializer):
    class Meta:
        model = systems
        fields = '__all__'

class genraSerializer(serializers.ModelSerializer):
    class Meta:
        model = genre
        fields = '__all__'

class messagesSerializer(serializers.ModelSerializer):
    class Meta:
        model = messages
        fields = '__all__'

class regionSerializer(serializers.ModelSerializer):
    class Meta:
        model = region
        fields = '__all__'

class postsSerializer(serializers.ModelSerializer):
    sender_uid = serializers.CharField(source='sender.uid', max_length=100, read_only=True)
    sender_data = serializers.SerializerMethodField()

    class Meta:
        model = posts
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
        post = posts.objects.create(**validated_data)

        return post
    
class flashCardSerialized(serializers.ModelSerializer):
    class Meta:
        model = flashcards
        fields = '__all__'