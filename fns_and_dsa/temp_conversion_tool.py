FAHRENHEIT_TO_CELSIUS_FACTOR = 5/9
CELSIUS_TO_FAHRENHEIT_FACTOR = 9/5

def convert_to_celsius(fahrenheit):
    return (fahrenheit - 32) * FAHRENHEIT_TO_CELSIUS_FACTOR

def convert_to_fahrenheit(celsius):
    return (celsius * CELSIUS_TO_FAHRENHEIT_FACTOR) + 32

if __name__ == "__main__":
    temp_input = input("Enter the temperature to convert: ")
    scale = input("Is this temperature in Celsius or Fahrenheit? (C/F): ").strip().upper()

    try:
        temp = float(temp_input)
    except ValueError:
        raise ValueError("Invalid temperature. Please enter a numeric value.")

    if scale == "F":
        result = convert_to_celsius(temp)
        print(f"{temp}°F is {result:.2f}°C")
    elif scale == "C":
        result = convert_to_fahrenheit(temp)
        print(f"{temp}°C is {result:.2f}°F")
    else:
        raise ValueError("Invalid scale. Please enter 'C' for Celsius or 'F' for Fahrenheit.")