from django.urls import path

from .views import PostList

app_name = 'post'
urlpatterns = [
    path('',PostList.as_view(),name='post_list'),
]
