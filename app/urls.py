from django.urls import path

from app.views import index

urlpatterns = [
    path('', index.as_view(), name='index'),
    path('post', index.as_view(), name='index'),  
]