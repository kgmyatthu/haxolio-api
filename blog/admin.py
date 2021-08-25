from django.contrib import admin
from blog.models import Category, Tag, Article
# Register your models here.


@admin.register(Article)
class ArticleAdmin(admin.ModelAdmin):
    list_display = ("id","title","unique_slug",)
    search_fields = ['title', 'unique_slug', ]
    readonly_fields = ('created_at','updated_at','unique_slug')

    class Meta:
       model = Article

@admin.register(Tag)
class TagAdmin(admin.ModelAdmin):
    list_display = ("id","name")
    search_fields = ("id","name")

    class Meta:
        model = Tag

@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ("id","name")
    search_fields = ("id","name")

    class Meta:
        model = Category