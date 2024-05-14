from rest_framework.pagination import PageNumberPagination
import math
from rest_framework.response import Response


class PagePagination(PageNumberPagination):
    page_size = 3 # розмір сторінки
    max_page_size = 10 # максимальний розмір сторінки
    page_size_query_param = 'size' # квері-парамс за допомогою якого можна вказувати к-сть між 3 і 10

    def get_paginated_response(self, data): # кастомізація стрічок prev, next, data (res)
        count = self.page.paginator.count # змінна, що рахує загальну к-сть машинок, paginator.count - підраховує скільки взагалі є карів
        total_pages = math.ceil(count//self.get_page_size(self.request)) # вираховуємо загальну к-сть сторінок count ділимо на page_size, так як page_size динамічний то тягнемо його з self
        # в get_page_size передаємо self.request, бо в request вписується к-сть на сторінку. Так яка виходить значення Float, то ми його округлюємо до більшого -> math.ceil
        return Response({ # віддаємо результати
            'total_items': count,
            'total_pages': total_pages,
            'prev': bool(self.get_previous_link()),
            'next': bool(self.get_next_link()),
            'data': data
        })

