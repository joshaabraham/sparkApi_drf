from django.urls import path
from . import views

urlpatterns = [
    path("chatsCreate/", views.ChatListCreateView.as_view(), name="chat_list_create"),
    path("chats/<int:pk>/", views.ChatRetrieveUpdateDestroyView.as_view(), name="chat_detail"),
    path("messagesCreate/", views.MessageListCreateView.as_view(), name="message_create"),
]