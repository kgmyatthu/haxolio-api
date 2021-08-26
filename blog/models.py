from django.db import models
from django.utils.text import slugify

# Create your models here.
class Tag(models.Model):
    class Meta:
        app_label = 'blog'
    name=models.CharField(max_length=30,blank=False,unique=True)
    def __str__(self):
        return self.name


class Category(models.Model):
    name = name=models.CharField(max_length=30,blank=False,unique=True)
    def __str__(self):
        return self.name


class Article(models.Model):

    title = models.TextField(max_length=1024,blank=False)
 
    tag = models.ManyToManyField(Tag,blank=False)
    category = models.ForeignKey(Category, on_delete=models.PROTECT, blank=False)

    markdown = models.TextField(null=True, blank=True)

    unique_slug = models.SlugField(max_length=2048,unique=True, null=False,editable=False)

    published = models.BooleanField(default=False, blank=False)
    featured = models.BooleanField(default=False, blank=False)

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title
    
    def save(self, *args, **kwargs):
        unique_slug = slugify(self.title)
        num = 1
        while Article.objects.filter(unique_slug=unique_slug).exists():
            unique_slug = f'{unique_slug}-{num}'
            num += 1
        self.unique_slug = unique_slug
        super(Article,self).save(*args, **kwargs)