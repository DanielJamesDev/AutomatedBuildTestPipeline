def validate_sensor_data(values, min_value=0.0, max_value=100.0):
    """
    Validates a list of numeric sensor values.
    Returns True if all values are within bounds; False if any are out of range.
    Raises errors if input is invalid.
    """
    if not isinstance(values, list):
        raise TypeError("Input must be a list")

    for value in values:
        if not isinstance(value, (int, float)):
            raise ValueError("All values must be numeric")
        if value < min_value or value > max_value:
            return False

    return True
