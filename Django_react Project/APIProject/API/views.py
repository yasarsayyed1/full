from django.contrib.auth.models import User
from rest_framework import viewsets
from .models import Article
from .serializer import ArticleSerializer, UserSerializer
from rest_framework.authentication import TokenAuthentication
from rest_framework.permissions import IsAuthenticated
# Create your views here.


class Articleview(viewsets.ModelViewSet):
    queryset=Article.objects.all()
    serializer_class=ArticleSerializer
    permission_classes=[IsAuthenticated]
    authentication_classes=(TokenAuthentication,)

class UserView(viewsets.ModelViewSet):
    queryset=User.objects.all()
    serializer_class=UserSerializer
    