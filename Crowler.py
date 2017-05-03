import os
from Domain import *
from IpAddress import *
from RobotsTxt import *


class Crowler(object):

    def __init__(self):
        pass

    @staticmethod
    def get_root_dir():
        return 'sites'

    @staticmethod
    def get_sites():
        return {
            'rabb': 'https://www.rabb.it/',  # multiple IPs
            'google': 'https://www.google.com.ua',
            'hneu': 'http://www.hneu.edu.ua/',
            'nure': 'http://nure.ua/'
        }

    @staticmethod
    def create_dir(directory):
        if not os.path.exists(directory):
            os.makedirs(directory)

    @staticmethod
    def write_file(path, data):
        f = open(path, 'w')
        f.write(data)
        f.close()

    @staticmethod
    def create_report(**kwargs):
        site_dir = Crowler.get_root_dir() + '/' + kwargs['name']
        Crowler.create_dir(site_dir)
        for i, j in kwargs.items():
            Crowler.write_file(site_dir + '/' + i + '.txt', j)

    @staticmethod
    def gather_info(name, url):
        domain = Domain.get_domain_name(url)
        report_args = {
            'name': name,
            'url': url,
            'domain_name': domain,
            'ip_address': IpAddress.get_ip_adress(domain, 'all'),
            'robots_txt': RobotsTxt.get_robots_txt(url)
        }

        Crowler.create_report(**report_args)

