from distances.models import House

def insert_house(price, address, url, image):
    house = House()
    house.price = price
    house.address = address
    house.link = url
    house.save()


def update_house(id, distance, duration, distance_to_dart, dart_sorting, near_by_dart):
    house = House.objects.get(pk=id)
    house.meters_walk_to_ov = distance
    house.time_walk_to_ov = duration
    house.time_walk_to_dart = distance_to_dart
    house.dart_for_sorting = dart_sorting
    house.dart_station = near_by_dart
    house.save()


def get_addresses():
    addresses = [(h.address, h.id) for h in House.objects.all()]
    return addresses
