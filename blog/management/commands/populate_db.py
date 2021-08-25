from django.core.management.base import BaseCommand
from faker import Faker
from blog.models import Category, Tag, Article
import random

class Command(BaseCommand):
    help = "Command info"
    
    def handle(self, *args, **kwargs):
        fake = Faker()
        number_of_entry_to_generate = 100
        tags = []
        categories = []

        for _ in range (0,8):
            tags.append(
                Tag.objects.create(name=fake.word())
            )
            categories.append(
                Category.objects.create(name=fake.word())
            )

        for i in range(number_of_entry_to_generate):
            article = Article.objects.create(
                    title = fake.paragraph(nb_sentences=2),
                    markdown = readme,
                    category = categories[random.randint(0,8-1)],
                    published = True,
                    featured = True,
                )

            for _ in range(0,random.randint(0,5)):
                article.tag.add(tags[random.randint(0,8-1)])

            article.save()
            completion = round((i/number_of_entry_to_generate)*100)
            print(f"{completion}%")

        print(f"100%")


readme = """
![python version](https://img.shields.io/badge/python-3.8-blue)
![pip moviepy](https://img.shields.io/badge/pip-moviepy-blue)

# What is this
  vdo2gif is a command line tool for converting video file into gif. I find myself opening video editing software just to do simple gif which i'd use to show examples in readme.md of my github repos. This tool is compitable with any python3 compitable system. Tested on windows 10 and linux-debian x86 machines.
### Features
 - custom fps, speed, size.
 
# Installation
  Install python3
  ```
  root@kali:~# sudo apt-get install python3
  ```
  Install dependencies 
  ```
  root@kali:~# sudo python3 -m pip -r requirement.txt
  ```
  Install pip if you see something like pip module not found.
  ```
    root@kali:~# sudo apt-get install python3-pip
  ```
  
 # Usage
 ### Converting the whole video file
 To convert the whole video file to gif
 ```
 usage: python3 vdo2gif.py /path/to/input.mp4 /path/to/output.gif 
 ```
This example convert the whole video file to gif.
 
 ![image1](https://static.wixstatic.com/media/4cbe8d_f1ed2800a49649848102c68fc5a66e53~mv2.gif)
 
 
 ### Converting only a specific part of the video file
  ```
 usage: python3 vdo2gif.py /path/to/input.mp4 /path/to/output.gif -t hr:min:sec hr:min:sec 
 ```
  This example convert only the part between 5sec and 9sec of the video file
  
 ![image1](https://static.wixstatic.com/media/4cbe8d_f1ed2800a49649848102c68fc5a66e53~mv2.gif)
  
  # REMINDER TO MYSELF ::
  -

"""