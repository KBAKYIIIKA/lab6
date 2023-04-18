from django.urls import path, re_path
from . import views


urlpatterns = [
    path('', views.archive, name='home'),
    re_path(r'^article/(?P<article_id>\d+)$', views.get_article, name='get_article'),
    path('article/new/', views.create_post, name='new'),
]
