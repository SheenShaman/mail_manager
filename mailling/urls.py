from django.urls import path
from django.views.decorators.cache import cache_page
from mailling.apps import MaillingConfig
from mailling.views import (MainView, MaillingCreateView, MaillingListView, MaillingDetailView, MaillingUpdateView, MaillingDeleteView,
                            MessageCreateView, MessageListView, MessageUpdateView, MessageDeleteView,
                            ClientCreateView, ClientListView, ClientUpdateView, ClientDeleteView,
                            LogsListView)

app_name = MaillingConfig.name

urlpatterns = [
    path('', MainView.as_view(), name='main'),
    path('mailling/create/', MaillingCreateView.as_view(), name='mailling_create'),
    path('maillings/', MaillingListView.as_view(), name='maillings'),
    path('mailling/detail/<int:pk>', MaillingDetailView.as_view(), name='mailling_detail'),
    path('mailling/update/<int:pk>', MaillingUpdateView.as_view(), name='mailling_update'),
    path('mailling/delete/<int:pk>', MaillingDeleteView.as_view(), name='mailling_delete'),

    path('message/create/', MessageCreateView.as_view(), name='message_create'),
    path('messages/', MessageListView.as_view(), name='messages'),
    path('message/update/<int:pk>', MessageUpdateView.as_view(), name='message_update'),
    path('message/delete/<int:pk>', MessageDeleteView.as_view(), name='message_delete'),

    path('client/create/', ClientCreateView.as_view(), name='client_create'),
    path('clients/', ClientListView.as_view(), name='clients'),
    path('client/update/<int:pk>', ClientUpdateView.as_view(), name='client_update'),
    path('client/delete/<int:pk>', ClientDeleteView.as_view(), name='client_delete'),

    path('logs/', LogsListView.as_view(), name='logs')
]
