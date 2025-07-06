import time
from adafruit_circuitplayground import cp


def CelToFahr(celsius):
    fahrenheit = (celsius * 9 / 5) + 32
    return fahrenheit


def FahrToCel(fahrenheit):
    celsius = (fahrenheit - 32) * 5 / 9
    return celsius


while True:
    current_temperature_celsius = cp.temperature
    if cp.switch:
        converted_temperature = CelToFahr(current_temperature_celsius)
        print(f"Temperature: {converted_temperature:.2f} F")
    else:
        temp_in_fahr_for_conversion = CelToFahr(current_temperature_celsius)
        converted_temperature = FahrToCel(temp_in_fahr_for_conversion)
        print(f"Temperature: {converted_temperature:.2f} C")
    time.sleep(0.5)
