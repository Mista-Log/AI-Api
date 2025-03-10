# from django.urls import path
# from . import views
# from .views import GeminiChatView

# urlpatterns = [
#     path('chat/', GeminiChatView.as_view(), name='gemini-chat'),
# ]

from django.urls import path
from .views import GeminiChatAPI

urlpatterns = [
    path('chat/', GeminiChatAPI.as_view(), name='gemini-chat-api'),
]