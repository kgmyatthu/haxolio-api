from rest_framework import routers, serializers, viewsets
from .models import Article, Tag, Category

class TagSerializer(serializers.ModelSerializer):
    class Meta:
        model = Tag
        exclude = ["id"]

class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        exclude = ["id"]

class ArticleSerializer(serializers.ModelSerializer):
    tag = serializers.SerializerMethodField()
    category = serializers.SerializerMethodField()
    class Meta:
        model = Article
        # fields = "__all__"
        exclude = ["id"]

    def get_tag(self, instance):
        names = []
        for tag in instance.tag.all():
            names.append(tag.name)
        return names

    def get_category(self, instance):
        id = instance.category.id
        obj = Category.objects.get(id=id)
        name = obj.name
        return name
