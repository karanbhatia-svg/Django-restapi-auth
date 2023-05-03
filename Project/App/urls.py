from django.urls import path
from .views import RegisterViewSet, LoginView, UserView, LogoutView
from rest_framework import routers

router = routers.DefaultRouter()
router.register('register', RegisterViewSet, basename='register')

urlpatterns = [
    path('login/', LoginView.as_view(), name='login'),
    path('user/', UserView.as_view(), name='user'),
    path('logout/', LogoutView.as_view(), name='logout')
]

urlpatterns += router.urls