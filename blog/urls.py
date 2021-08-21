from .views import *
from django.urls import path
urlpatterns = [
    path("", api_get_articles, name="list"),
    path("<slug>/", api_get_article_detail, name="detail"),
]
