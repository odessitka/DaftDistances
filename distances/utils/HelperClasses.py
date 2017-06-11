import googlemaps

GOOGLE_KEY = 'AIzaSyDtDQB41Vx7014RMCBqXiQQctjCE9FIs74'

dart_stations = ["Grand Canal Dock Train Station","Lansdowne Road Train Station", "Sandymount Train Station",
                "Sydney Parade Train Station", "Blackrock Train Station","Booterstown Train Station",
                "Seapoint Train Station", "Salthill And Monkstown Train Station","Dun Laoghaire (Mallin) Station", "Sandycove & Glasthule Dart Station" ]


class CommuteMatrix:
    def __init__(self, origin_address, destination_address):
        self.destination_address = destination_address
        self.origin_address = origin_address
        matrix = self.get_distance_duration_matrix()
        self.__distance = matrix[0]
        self.__duration = int((matrix[0])*60/5000)
        #self.__sorting_time = matrix[2]
        dart = self.get_dart_distance_matrix()
        print(dart)
        self.__time_to_dart = dart[0]
        self.__dart_sorting = dart[1]
        #cleaning address of Dart (near_by_dart) from extra information
        self.__near_by_dart = dart[2].split(",")[0]

    # print(dart) results:
    # {'destination_addresses': ['Block 1, Blackrock Business Park, Blackrock, Dublin, Ireland'],
    #  'origin_addresses': ['Clarinda Park W, Glasthule, Dublin, Ireland'], 'rows': [{'elements': [
    #     {'distance': {'text': '4.0 km', 'value': 3970}, 'duration': {'text': '12 mins', 'value': 690},
    #      'status': 'OK'}]}], 'status': 'OK'}
    # ('0.6 km', 561, 'Sandycove & Glasthule Dart Station, Bóthar Chnoc an Línsigh, Dún Laoghaire, Dublin, Ireland')
    #
    # {'destination_addresses': ['Block 1, Blackrock Business Park, Blackrock, Dublin, Ireland'],
    #  'origin_addresses': ['6 Stradbrook Rd, Mountashton, Blackrock, Co. Dublin, A94 V5W6, Ireland'], 'rows': [{ 'elements': [
    #     { 'distance': {'text': '2.8 km','value': 2763},'duration': {'text': '7 mins', 'value': 410},
    #       'status': 'OK'}]}], 'status': 'OK'}
    # ('2.2 km', 2201, 'Longford Terrace, Monkstown, Co. Dublin, Ireland')


    @property
    def distance(self):
        return self.__distance

    @property
    def duration(self):
        return self.__duration

    @property
    def time_to_dart(self):
        return self.__time_to_dart

    @property
    def dart_sorting(self):
        return self.__dart_sorting

    @property
    def near_by_dart(self):
        return self.__near_by_dart

    def get_distance_duration_matrix(self):
        gmaps = googlemaps.Client(key=GOOGLE_KEY)
        matrix = gmaps.distance_matrix(self.origin_address, self.destination_address, transit_mode="walking")
        print(matrix)
        return matrix["rows"][0]["elements"][0]["distance"]["value"], matrix["rows"][0]["elements"][0]["duration"]["text"], matrix["rows"][0]["elements"][0]["duration"]["value"]

    def get_dart_distance_matrix(self):
        gmaps = googlemaps.Client(key=GOOGLE_KEY)
        matrix = gmaps.distance_matrix(self.origin_address, dart_stations, transit_mode="walking")

        combined = dict(zip(dart_stations, matrix["rows"][0]["elements"]))
        station_distances = enumerate(matrix["rows"][0]["elements"])
        sorted_distances = sorted(station_distances, key=lambda x: x[1]["distance"]["value"])
        index = sorted_distances[0][0]
        return sorted_distances[0][1]["distance"]["text"], sorted_distances[0][1]["distance"]["value"], matrix["destination_addresses"][index]


class HelperHouse:
    def __init__(self, box):
        ad_a = box.find("a")
        address_full = ad_a.text
        add = address_full.split("-")
        self.__address = add[0].strip()
        self.__url = ('http://www.daft.ie' + ad_a.get("href"))
        get_image = box.find("img")
        self.__image = get_image.get("data-original")
        self.__price = box.find("strong", "price").text

    @property
    def address(self):
        return self.__address

    @property
    def url(self):
        return self.__url

    @property
    def image(self):
        return self.__image

    @property
    def price(self):
        return self.__price
