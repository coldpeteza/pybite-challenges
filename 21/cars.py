from typing import Dict, List
import re

cars = {
    'Ford': ['Falcon', 'Focus', 'Festiva', 'Fairlane'],
    'Holden': ['Commodore', 'Captiva', 'Barina', 'Trailblazer'],
    'Nissan': ['Maxima', 'Pulsar', '350Z', 'Navara'],
    'Honda': ['Civic', 'Accord', 'Odyssey', 'Jazz'],
    'Jeep': ['Grand Cherokee', 'Cherokee', 'Trailhawk', 'Trackhawk']
}
DEFAULT_SEARCH = "trail"
CarsType = Dict[str, List[str]]


def get_all_jeeps(cars: CarsType = cars) -> str:
    """
    Retrieve the 'Jeep' models from the cars dict and join them by a
    comma and space (', '). Leave the original ordering intact.
    """
    just_jeeps = cars.copy()

    results = ', '.join(just_jeeps['Jeep'])

    return results


def get_first_model_each_manufacturer(cars: CarsType = cars) -> List[str]:
    """
    Loop through the cars dict filtering out the first model for each
    manufacturer. Return the matching models in a list leaving the original
    ordering intact.
    """
    result = []
    manufacturers = cars.copy()

    for manufacturer in manufacturers.values():
        result.append(manufacturer[0])

    return result


def get_all_matching_models(
    cars: CarsType = cars, grep: str = DEFAULT_SEARCH
) -> List[str]:
    """
    Return a list of all models containing the case insensitive
    'grep' string which defaults to DEFAULT_SEARCH ('trail').
    Sort the resulting sequence alphabetically
    """
    trails = cars.copy()
    result = []
    regex = re.compile(grep, flags=re.IGNORECASE)
    for model_list in trails.values():
        for model in model_list:
            check = re.search(regex, model)
            if check is not None:
                result.append(model)
    result.sort()
    return result

def sort_car_models(cars: CarsType = cars) -> CarsType:
    """
    Loop through the cars dict returning a new dict with the
    same keys and the values sorted alphabetically.
    """
    sorted_cars = cars.copy()
    for brand in sorted_cars.keys():
        sorted_cars[brand] = sorted(sorted_cars[brand])

    return sorted_cars