# Haxolio-api

This is a mini blogging api server written in python Django Rest Framework to powered one of my react portfolio theme called [haxolio](https://github.com/kmt29/haxolio). Haxolio-api has a built in django admin panel with solid authentication most suitable for personal uses. 

# Usage

Haxolio-api provide 4 main feature. 

## Fetching all article in one batch
`/blog/all` this api returns a list of all the available articles
### Response example
```json
[
    {
        "tag": [
            "heart",
            "may"
        ],
        "category": "American",
        "title": "Really help west operation heart table then determine. Relate financial phone scene boy wide but.",
        "markdown": "markdown",
        "unique_slug": "really-help-west-operation-heart-table-then-determine-relate-financial-phone-scene-boy-wide-but-1",
        "published": true,
        "featured": true,
        "created_at": "2021-08-26T13:14:23.058234Z",
        "updated_at": "2021-08-26T13:14:25.992687Z"
    }
]
```
## Fetching paginated list of all article available

`/blog` this api returns a paginated list of all available articles

### Response example
```json
{
    "count": 100,
    "next": "http://localhost/blog/?page=2",
    "previous": null,
    "results": [
        {
            "tag": [
                "pay"
            ],
            "category": "American",
            "title": "Age personal available garden worry what audience.",
            "markdown": "\n# A demo of ...",
            "unique_slug": "age-personal-available-garden-worry-what-audience-1",
            "published": true,
            "featured": true,
            "created_at": "2021-08-26T13:23:12.083453Z",
            "updated_at": "2021-08-26T13:23:15.063933Z"
        }
    ]
}
```

## Searching Article 

`/blog/search/{keyword}` this api return a list of article according to searched keyword. Keyword is search against article's title, tag, and category.

# Getting the server started locally

This is a python project powered by python 3.8. Python 3.8 is required to install on the machine.
Once python 3.8 is ensure to install on the machine, proceed to further steps.

## Get this repo locally
`git clone https://github.com/kmt29/haxolio-api.git` 

## cd into directory
`cd haxolio-api`

## Install required python dependencies
`pip install -r requirements.txt`

## Set enviroment variables
Environment variables are require to set such as secret key, and database credentials.
you can either create KEYS.json in repo's root folder or set the environment variable.

`PRODUCTION NOTE:` if you're using app engine such as heroku, KEYS.json probably won't work and you'll need to set environment variable

### KEYS.json
```json
{   
    "DEBUG" : "TRUE",
    "SECRET_KEY": "yoursecretkey",

    "DB_NAME": "asldkf",
    "DB_HOST": "ec2-54-dcompute.amazonaws.com",
    "DB_PORT": "5432",
    "DB_USER": "admin",
    "DB_PASSWORD": "password",

    "DB_NAME_DEV": "asldkf",
    "DB_HOST_DEV": "ec2-54-dcompute.amazonaws.com",
    "DB_PORT_DEV": "5432",
    "DB_USER_DEV": "admin",
    "DB_PASSWORD_DEV": "password"
}
```

### Generating secret key
`python -c 'from django.core.management.utils import get_random_secret_key; print(get_random_secret_key())'`
Use a secret key consistently throughout the whole production or development. 

## Set CORS 

In `/core/settings.py`, add a list of domain name you want your api to response to
```python
CORS_ALLOWED_ORIGINS = [

    "http://localhost:3000",
    "https://www.yoursite.com",
    "https://mysite.com"
    "https://example.com"

]
```
# Code of conduct 
You're free to use for both commercial and personal usage under appropriate credit.

