from tld import get_tld  # $ pip install tld
from Crowler import *


class Domain(object):

    def __init__(self):
        pass

    @staticmethod
    def get_domain_name(url):
        domain_name = get_tld(url)
        return domain_name
