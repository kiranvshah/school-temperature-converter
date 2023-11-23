def convert_temp(value: float, original_unit: str, destination_unit: str):
    # convert original unit to Celsius
    match original_unit:
        case 'celsius':
            celsius = value
        case 'kelvin':
            celsius = value - 273.15
        case 'fahrenheit':
            celsius = (value - 32) * (5 / 9)
        case 'rankine':
            celsius = (value - 491.67) * (5 / 9)
        case _:
            raise ValueError('Provided original_unit was not known')

    # convert from celsius to destination unit
    match destination_unit:
        case 'celsius':
            destination_value = celsius
        case 'kelvin':
            destination_value = celsius + 273.15
        case 'fahrenheit':
            destination_value = (celsius * (9 / 5)) + 32
        case 'rankine':
            destination_value = celsius * (9 / 5) + 491.67
        case _:
            raise ValueError('Provided destination_unit was not known')

    return destination_value
