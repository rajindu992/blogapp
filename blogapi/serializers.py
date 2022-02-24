from rest_framework.serializers import ModelSerializer
from posts.models import Article

from authapp.models import MyUser
from rest_framework import serializers


class ArticleSerializer(ModelSerializer):
    author = serializers.CharField(read_only=True)

    class Meta:
        model = Article
        fields = ['author','title', 'body', 'created_on']

    def create(self, validated_data):
        return Article.objects.create(**validated_data)


class UserRegistrationSerializer(ModelSerializer):
    class Meta:
        model = MyUser
        fields = ['full_name', 'email', 'phone', 'password']

    def create(self, validated_data):
        return MyUser.objects.create_user(email=validated_data['email'], full_name=validated_data['full_name'],
                                          phone=validated_data['phone'], password=validated_data['password'])


class LoginSerializer(serializers.Serializer):
    email = serializers.CharField()
    password = serializers.CharField()
