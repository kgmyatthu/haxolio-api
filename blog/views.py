from blog.serializers import ArticleSerializer
from django.shortcuts import render
from .models import Article
from .serializers import ArticleSerializer
from .paginators import CustomPagination

from rest_framework import status
from rest_framework.response import Response
from rest_framework.decorators import api_view
from django.contrib.postgres.search import SearchVector

@api_view(['GET'])
def api_get_article_detail(request, slug):
    if request.method == "GET":
        try:
            article = Article.objects.get(unique_slug=slug,published=True)
            serializer = ArticleSerializer(article)
            return Response(serializer.data)
        except:
            return Response(status=status.HTTP_404_NOT_FOUND)

@api_view(['GET'])
def api_get_paginated_articles(request):
    try:
        article = Article.objects.filter(published=True).order_by("-updated_at")

        if len(article) > 0:
            paginator = CustomPagination()
            result_page = paginator.paginate_queryset(article,request)

            serializer = ArticleSerializer(result_page, many=True)
            return paginator.get_paginated_response(serializer.data)

    except:
        return Response(status=status.HTTP_404_NOT_FOUND)

@api_view(['GET'])
def api_get_all_articles(request):
    try:
        article = Article.objects.filter(published=True)
        if len(article) > 0:
            serializer = ArticleSerializer(article, many=True)
            return Response(serializer.data)

    except:
        return Response(status=status.HTTP_404_NOT_FOUND)

@api_view(['GET'])
def api_get_search_articles(request,keyword):
    try:
        article = Article.objects.annotate(
            search=SearchVector("title", "category__name", "tag__name")
        ).filter(search=keyword,published=True)
        if len(article) > 0:
            serializer = ArticleSerializer(article, many=True)
            return Response(serializer.data)

    except:
        return Response(status=status.HTTP_404_NOT_FOUND)