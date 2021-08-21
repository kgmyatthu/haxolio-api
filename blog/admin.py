from django.contrib import admin
from blog.models import Tag, Article
# Register your models here.

admin.site.register(Tag)

@admin.register(Article)
class ArticleAdmin(admin.ModelAdmin):
    list_display = ("id","title","unique_slug",)
    search_fields = ['title', 'unique_slug', ]
    readonly_fields = ('created_at','updated_at','unique_slug')

    class Meta:
       model = Article