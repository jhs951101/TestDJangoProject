from django.urls import path
from .scripts import home

urlpatterns = [
    path('get/', home.get, name='get'),
    path('post/', home.post, name='post'),
    path('postjson/', home.postjson, name='postjson'),
];