from .views import *
from django.urls import path
urlpatterns = [
    path("", api_get_paginated_articles, name="list"),
    path("all/", api_get_all_articles, name="full_list"),
    path("<slug>/", api_get_article_detail, name="detail"),
]
