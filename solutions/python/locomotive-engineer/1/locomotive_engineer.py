"""Functions which helps the locomotive engineer to keep track of the train."""


def get_list_of_wagons(*args):
    """Return a list of wagons.

    :param: arbitrary number of wagons.
    :return: list - list of wagons.
    """
    [*wagons] = args
    return wagons


def fix_list_of_wagons(each_wagons_id, missing_wagons):
    """Fix the list of wagons.

    :param each_wagons_id: list - the list of wagons.
    :param missing_wagons: list - the list of missing wagons.
    :return: list - list of wagons.
    """
    wagonA, wagonB, wagonC, *rest = each_wagons_id
    return [wagonC, *missing_wagons] + [*rest, wagonA, wagonB]


def add_missing_stops(route, **stops):
    """Add missing stops to route dict.

    :param route: dict - the dict of routing information.
    :param: arbitrary number of stops.
    :return: dict - updated route dictionary.
    """
    stop_list = []
    stop_dict = dict(stops)
    for item in stop_dict:
        stop_list.append(stop_dict.get(item))
    new_stops = {'stops':stop_list}
    res = {**route, **new_stops}
    return res
    


def extend_route_information(route, more_route_information):
    """Extend route information with more_route_information.

    :param route: dict - the route information.
    :param more_route_information: dict -  extra route information.
    :return: dict - extended route information.
    """
    return {**route, **more_route_information}


def fix_wagon_depot(wagons_rows):
    """Fix the list of rows of wagons.

    :param wagons_rows: list[list[tuple]] - the list of rows of wagons.
    :return: list[list[tuple]] - list of rows of wagons.
    """

    switched_wagons = zip(*wagons_rows)
    fixed = []
    for wagons in switched_wagons:
        fixed.append(list(wagons))

    return fixed
