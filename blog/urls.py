from django.urls import path, include
from .views import RegisterView, BlogViewSet, LogoutView
from rest_framework.routers import DefaultRouter


router = DefaultRouter()
router.register(r'blogs', BlogViewSet, basename='blog')

urlpatterns = [
    path('register/', RegisterView.as_view()),
    path('logout/', LogoutView.as_view()),
    path('', include(router.urls)),
]
