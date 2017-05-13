import urllib, re, sqlite3, googlemaps
from bs4 import BeautifulSoup
from Distances.utils import dbhelpers, HelperClasses
import logging
price = 1850
areas = 'blackrock,booterstown,dun-laoghaire,monkstown,sandymount'
url = "http://www.daft.ie/dublin-city/residential-property-for-rent/{0}/?s%5Bmxp%5D={1}&s%5Badvanced%5D=1&rental_tab_name=advanced-sf&searchSource=rental&offset={2}"
one_view = "oneview, blackrock"
logger = logging.getLogger(__name__)


def main():
    extract_and_insert()
    calc_distances()


def calc_distances():
    addresses = dbhelpers.get_addresses()
    for (address, id) in addresses:
        try:
            matrix = HelperClasses.CommuteMatrix(address, one_view)
            dbhelpers.update_house(id, matrix.distance, matrix.duration, matrix.time_to_dart,
                                   matrix.dart_sorting, matrix.near_by_dart)
        except Exception as e:
            logger.exception(e.__str__())
            pass


def extract_and_insert():
    offset = 0
    while True:
        html_of_search = urllib.request.urlopen(url.format(areas, price, offset)).read()
        soup_of_search = BeautifulSoup(html_of_search, "html5lib")
        boxes = soup_of_search.find_all('div', "box")
        if len(boxes) == 0: break
        for box in boxes:
            house = HelperClasses.House(box)
            dbhelpers.insert_house(house.price, house.address, house.url, house.image)
        offset += 20
