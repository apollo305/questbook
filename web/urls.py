from django.urls import path
from .views import *

urlpatterns = [
    path('', MessageList.as_view(), name = 'msg_list'),
    #message/
    path('<int:pk>/', MessageDetail.as_view(), name = 'msg_view'),
    #message/<int:pk>/
    #message/5/
    path('create/', MessageCreate.as_view(), name = 'msg_create')
    #message/create/
]