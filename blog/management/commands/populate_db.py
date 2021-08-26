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
# A demo of `react-markdown`

`react-markdown` is a markdown component for React.

👉 Changes are re-rendered as you type.

👈 Try writing some markdown on the left.

## Overview

* Follows [CommonMark](https://commonmark.org)
* Optionally follows [GitHub Flavored Markdown](https://github.github.com/gfm/)
* Renders actual React elements instead of using `dangerouslySetInnerHTML`
* Lets you define your own components (to render `MyHeading` instead of `h1`)
* Has a lot of plugins

## Table of contents

Here is an example of a plugin in action
([`remark-toc`](https://github.com/remarkjs/remark-toc)).
This section is replaced by an actual table of contents.

## Syntax highlighting

Here is an example of a plugin to highlight code:
[`rehype-highlight`](https://github.com/rehypejs/rehype-highlight).

```js
import React from 'react'
import ReactDOM from 'react-dom'
import ReactMarkdown from 'react-markdown'
import rehypeHighlight from 'rehype-highlight'

ReactDOM.render(
  <ReactMarkdown rehypePlugins={[rehypeHighlight]}>{'# Your markdown here'}</ReactMarkdown>,
  document.querySelector('#content')
)
```

Pretty neat, eh?

## GitHub flavored markdown (GFM)

For GFM, you can *also* use a plugin:
[`remark-gfm`](https://github.com/remarkjs/react-markdown#use).
It adds support for GitHub-specific extensions to the language:
tables, strikethrough, tasklists, and literal URLs.

These features **do not work by default**.
👆 Use the toggle above to add the plugin.

| Feature    | Support              |
| ---------: | :------------------- |
| CommonMark | 100%                 |
| GFM        | 100% w/ `remark-gfm` |

~~strikethrough~~

* [ ] task list
* [x] checked item

https://example.com

## HTML in markdown

⚠️ HTML in markdown is quite unsafe, but if you want to support it, you can
use [`rehype-raw`](https://github.com/rehypejs/rehype-raw).
You should probably combine it with
[`rehype-sanitize`](https://github.com/rehypejs/rehype-sanitize).

<blockquote>
  👆 Use the toggle above to add the plugin.
</blockquote>

## Components

You can pass components to change things:

```js
import React from 'react'
import ReactDOM from 'react-dom'
import ReactMarkdown from 'react-markdown'
import MyFancyRule from './components/my-fancy-rule.js'

ReactDOM.render(
  <ReactMarkdown
    components={{
      // Use h2s instead of h1s
      h1: 'h2',
      // Use a component instead of hrs
      hr: ({node, ...props}) => <MyFancyRule {...props} />
    }}
  >
    # Your markdown here
  </ReactMarkdown>,
  document.querySelector('#content')
)
```

## More info?

Much more info is available in the
[readme on GitHub](https://github.com/remarkjs/react-markdown)!

***

A component by [Espen Hovlandsdal](https://espen.codes/)
"""












"""
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