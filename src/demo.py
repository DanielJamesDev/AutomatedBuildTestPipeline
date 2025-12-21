from src.data_validator import validate_sensor_data

# Example sensor streams
temperature_data = [22.5, 23.1, 21.9, 99.9]  # last value outlier
pressure_data = [101.3, 100.8, 102.0, 101.5]

results = {
    "Temperature valid": validate_sensor_data(temperature_data, 0, 50),
    "Pressure valid": validate_sensor_data(pressure_data, 90, 110)
}

# Save results to outputs/demo_results.txt
with open("../outputs/demo_results.txt", "w") as f:
    for key, value in results.items():
        f.write(f"{key}: {value}\n")

# Print results to console
for key, value in results.items():
    print(f"{key}: {value}")
