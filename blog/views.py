from blog.serializers import ArticleSerializer
from django.shortcuts import render
from .models import Article
from .serializers import ArticleSerializer
from .paginators import CustomPagination

from rest_framework import status
from rest_framework.response import Response
from rest_framework.decorators import api_view
# from rest_framework.generics import ListAPIView

# Create your views here.

@api_view(['GET'])
def api_get_article_detail(request, slug):
    if request.method == "GET":
        try:
            article = Article.objects.get(unique_slug=slug)
            serializer = ArticleSerializer(article)
            return Response(serializer.data)
        except Article.DoesNotExist:
            return Response(status=status.HTTP_404_NOT_FOUND)

@api_view(['GET'])
def api_get_articles(request):
    try:
        article = Article.objects.all()

        if len(article) > 0:
            paginator = CustomPagination()
            result_page = paginator.paginate_queryset(article,request)

            serializer = ArticleSerializer(result_page, many=True)
            return paginator.get_paginated_response(serializer.data)

    except Article.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)