from typing import OrderedDict
from rest_framework import pagination
from rest_framework.response import Response
from collections import OrderedDict

class CustomPagination(pagination.PageNumberPagination):
    page_size = 30
    page_size_query_param = 'per_page'
    max_page_size = 80
    page_query_param = 'page'

def get_paginated_response(self, data):
        return Response(
            OrderedDict(
                [
                    (
                        "links",
                        {
                            "next": self.get_next_link(),
                            "previous": self.get_previous_link(),
                        },
                    ),
                    ("count", self.page.paginator.count),
                    ("total_pages", self.page.paginator.num_pages),
                    ("page", self.page.number),
                    ("results", data),
                ]
            )
        ) 