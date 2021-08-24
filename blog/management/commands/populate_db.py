from django.core.management.base import BaseCommand
from faker import Faker
from blog.models import Tag, Article
import random

class Command(BaseCommand):
    help = "Command info"
    
    def handle(self, *args, **kwargs):
        fake = Faker()
        
        for _ in range(200):
            
            article = Article.objects.create(
                    title = fake.paragraph(nb_sentences=2),
                    markdown = fake.paragraph(nb_sentences=100),
                    published = True,
                    featured = True,
                )

            tag1 = Tag.objects.create(name=fake.license_plate())
            tag2 = Tag.objects.create(name=fake.license_plate())

            article.tag.add(tag1,tag2)
            article.save()