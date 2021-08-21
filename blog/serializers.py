from rest_framework import routers, serializers, viewsets
from .models import Article, Tag 

class TagSerializer(serializers.ModelSerializer):
    class Meta:
        model = Tag
        exclude = ["id"]

class ArticleSerializer(serializers.ModelSerializer):
    tag = serializers.SerializerMethodField()
    class Meta:
        model = Article
        # fields = "__all__"
        exclude = ["id"]

    def get_tag(self, instance):
        names = []
        for tag in instance.tag.all():
            names.append(tag.name)
        return names
