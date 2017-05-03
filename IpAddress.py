import socket


class IpAddress(object):

    @staticmethod
    def get_ip_adress(url, qty="all"):
        ip_list = []
        ais = socket.getaddrinfo(url, 0, 0, 0, 0)
        for result in ais:
            ip_list.append(result[-1][0])
            ip_list = list(set(ip_list))
        if qty == "first":
            return ip_list[0]
        elif qty == "all":
            return str(ip_list)
        else:
            return False
