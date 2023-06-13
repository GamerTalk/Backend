from rest_framework import serializers
from base.models import Users, english, spanish, french, german, japanese, chinese, korean, systems, genre, messages, region, posts


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
    class Meta:
        model = posts
        fields = '__all__'
