from django.urls import path
from django.urls.conf import include
from .views import  Articleview, UserView
from rest_framework.routers import DefaultRouter

router = DefaultRouter()
router.register('articles', Articleview, basename='article')
router.register('user',UserView)



urlpatterns = [
    path('api/',include(router.urls))
]