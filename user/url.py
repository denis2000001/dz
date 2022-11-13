from django.urls import path
from user.views import *

urlpatterns = [
    path('login/', LoginCreateAPIView.as_view()),
    path('register/', RegisterCreateAPIView.as_view())

]
