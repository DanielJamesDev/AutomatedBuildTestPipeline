import pytest
from src.data_validator import validate_sensor_data

def test_valid_data():
    assert validate_sensor_data([10, 20, 30]) is True

def test_out_of_range_data():
    assert validate_sensor_data([10, -5, 30]) is False

def test_non_numeric_data():
    with pytest.raises(ValueError):
        validate_sensor_data([10, "bad", 30])

def test_invalid_input_type():
    with pytest.raises(TypeError):
        validate_sensor_data("not a list")
