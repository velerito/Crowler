from Crowler import *


def gather_init():
    Crowler.create_dir(Crowler.get_root_dir())
    for name, url in Crowler.get_sites().items():
        Crowler.gather_info(name, url)


gather_init()
