from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status, permissions, generics, authentication
from rest_framework.authtoken.models import Token


from posts.models import Article
from blogapi.serializers import ArticleSerializer, UserRegistrationSerializer, LoginSerializer

from django.contrib.auth import authenticate, login, logout


class ArticleCreate(APIView):

    permission_classes = [permissions.IsAuthenticated]
    def get(self, request, *args, **kwargs):
        articles = Article.objects.all()
        serializer = ArticleSerializer(articles, many=True)
        return Response(serializer.data)

    def post(self, request, *args, **kwargs):
        serializer = ArticleSerializer(data=request.data,context={'author':request.user})
        if serializer.is_valid():
            article = serializer.save()
            article.save
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        else:
            return Response(status=status.HTTP_400_BAD_REQUEST)


class ArticleDetail(APIView):

    permission_classes = [permissions.IsAuthenticated]
    def get_object(self,id):
        return Article.objects.get(id=id)

    def get(self,request, *args, **kwargs):
        id = kwargs['id']
        article = self.get_object(id=id)
        serializer = ArticleSerializer(article)
        return Response(serializer.data, status=status.HTTP_200_OK)

    def put(self, request, *args, **kwargs):
        article = self.get_object(kwargs['id'])
        serializer = ArticleSerializer(instance=article, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        else:
            return Response(serializer.data, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, *args, **kwargs):
        id = kwargs['id']
        article = self.get_object(id=id)
        article.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)


class UserRegistrationView(APIView):
    def post(self, request, *args, **kwargs):
        serializer = UserRegistrationSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class LoginView(APIView):
    def post(self, request, *args, **kwargs):
        serializer = LoginSerializer(data=request.data)
        if serializer.is_valid():
            username = serializer.validated_data['email']
            password = serializer.validated_data['password']
            user = authenticate(request, username=username, password=password)
            if user:
                login(request, user)
                token,created = Token.objects.get_or_create(user=user)
                return Response({'token':token.key},status=status.HTTP_200_OK)
            else:
                return Response({'message:authentication failed'}, status=status.HTTP_400_BAD_REQUEST)


class LogOut(APIView):
    def get(self, request):
        logout(request)
        return Response({'msg': "session ended"})
