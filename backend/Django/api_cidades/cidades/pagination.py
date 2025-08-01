from rest_framework import pagination


class CustomPagination(pagination.PageNumberPagination):
    page_size = 10
    max_page_size = 100
    page_size_query_param = 'take'
    page_query_param = 'page'
