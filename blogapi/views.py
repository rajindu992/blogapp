from rest_framework.permissions import IsAuthenticated
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status, permissions, generics, authentication, mixins
from rest_framework.authtoken.models import Token

from posts.models import Article
from blogapi.serializers import ArticleSerializer, UserRegistrationSerializer, LoginSerializer

from django.contrib.auth import authenticate, login, logout


class ArticleCreate(generics.ListCreateAPIView):
    queryset = Article.objects.all()
    serializer_class = ArticleSerializer
    permission_classes = (IsAuthenticated,)

    def perform_create(self, serializer):
        serializer.save(author=self.request.user)


class ArticleDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Article.objects.all()
    serializer_class = ArticleSerializer
    permission_classes = [IsAuthenticated]


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
                token, created = Token.objects.get_or_create(user=user)
                return Response({'message:authentication successful'}, status=status.HTTP_200_OK)
            else:
                return Response({'message:authentication failed'}, status=status.HTTP_400_BAD_REQUEST)


class LogOut(APIView):
    def get(self, request):
        logout(request)
        return Response({'msg': "session ended"})
