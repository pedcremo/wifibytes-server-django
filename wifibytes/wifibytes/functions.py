# encoding:utf-8
from rest_framework import pagination


class LargeResultsSetPagination(pagination.PageNumberPagination):
    page_size = 20
    page_size_query_param = 'page_size'
    max_page_size = 10000


def calculate_checksum(partial_icc):

    def luhn_checksum(icc):

        def digits_of(number):
            return [int(i) for i in str(number)]

        digits = digits_of(icc)
        odd_digits = digits[-1::-2]
        even_digits = digits[-2::-2]
        total = sum(odd_digits)
        for digit in even_digits:
            total += sum(digits_of(2 * digit))
        return total % 10

    check_digit = luhn_checksum(int(partial_icc) * 10)
    return check_digit if check_digit == 0 else 10 - check_digit


def get_full_image_url(request, path):
    secure = 'http://'
    if request.is_secure():
        secure = 'https://'
    
    return "%s%s/%s" % (secure, request.get_host(), path)
