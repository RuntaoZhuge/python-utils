import hashlib
from datetime import datetime
from decimal import Decimal

def remove_prefix(string):
    return string.rsplit("/", 1)[-1]

def format_date(delta_date):
    if delta_date is None:
        return None

    try:
        date_string = str(delta_date)
        date = datetime.strptime(date_string, "%Y-%m-%d %H:%M:%S")
        return date.date().isoformat()
    except TypeError:
        return date_string


def round_to_4_decimal_places(string_number):
    try:
        number = float(string_number)
        rounded_number = round(number, 4)
        return "{:.4f}".format(rounded_number)
    except TypeError:
        # Handle the case when the input string cannot be converted to a float
        return None


def round_to_2_decimal_places(string_number):
    try:
        number = float(string_number)
        rounded_number = round(number, 2)
        return "{:.2f}".format(rounded_number)
    except TypeError:
        # Handle the case when the input string cannot be converted to a float
        return None


def generate_hash_id(unique_name, signature):
    input_string = unique_name
    md5 = hashlib.md5()
    md5.update(input_string.encode())
    unique_id = f"{signature}_{md5.hexdigest()}"
    return unique_id


def estimated_mapping(value):
    mapping = {
        "U": None,
        "A": 0,
        "E": 1,
        "N": 2,
    }
    if value in mapping:
        return mapping[value]
    else:
        return None

def stringify_value(value):
    return str(value) if value is not None else None
