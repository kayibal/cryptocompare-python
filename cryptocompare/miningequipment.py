from .helper_functions import load_data


def get_miningequipment():
    return load_data('https://www.cryptocompare.com/api/data/miningequipment/')