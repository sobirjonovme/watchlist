from rest_framework.pagination import PageNumberPagination
from rest_framework.response import Response


class FilmPagination(PageNumberPagination):
    page_size = 3
    page_size_query_param = 'page_size'
    max_page_size = 5

    def get_paginated_response(self, data):
        return Response({
            'links': {
                'next': super().get_next_link(),
                'previous': super().get_previous_link()
            },
            'total_elements': self.page.paginator.count,
            'total_pages': self.page.paginator.num_pages,
            'page': super().get_page_number(self.request, self.page.paginator),
            'page_size': super().get_page_size(self.request),
            'results': data
        })
