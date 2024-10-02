def length_converter(value, from_unit, to_unit):
    units = {
        'meters': 1,
        'kilometers': 1000,
        'centimeters': 0.01,
        'millimeters': 0.001,
        'inches': 0.0254,
        'feet': 0.3048,
        'yards': 0.9144,
        'miles': 1609.34
    }
    
    if from_unit not in units or to_unit not in units:
        raise ValueError("Unsupported unit for length conversion.")
    
    # Convert the input value to meters
    value_in_meters = value * units[from_unit]
    
    # Convert meters to the target unit
    converted_value = value_in_meters / units[to_unit]
    return converted_value

def weight_converter(value, from_unit, to_unit):
    units = {
        'grams': 1,
        'kilograms': 1000,
        'milligrams': 0.001,
        'pounds': 453.592,
        'ounces': 28.3495
    }
    
    if from_unit not in units or to_unit not in units:
        raise ValueError("Unsupported unit for weight conversion.")
    
    # Convert the input value to grams
    value_in_grams = value * units[from_unit]
    
    # Convert grams to the target unit
    converted_value = value_in_grams / units[to_unit]
    return converted_value

def temperature_converter(value, from_unit, to_unit):
    if from_unit == to_unit:
        return value
    
    if from_unit == 'celsius':
        if to_unit == 'fahrenheit':
            return (value * 9/5) + 32
        elif to_unit == 'kelvin':
            return value + 273.15
        else:
            raise ValueError("Unsupported target unit for temperature.")
    elif from_unit == 'fahrenheit':
        if to_unit == 'celsius':
            return (value - 32) * 5/9
        elif to_unit == 'kelvin':
            return (value - 32) * 5/9 + 273.15
        else:
            raise ValueError("Unsupported target unit for temperature.")
    elif from_unit == 'kelvin':
        if to_unit == 'celsius':
            return value - 273.15
        elif to_unit == 'fahrenheit':
            return (value - 273.15) * 9/5 + 32
        else:
            raise ValueError("Unsupported target unit for temperature.")
    else:
        raise ValueError("Unsupported unit for temperature conversion.")

def main():
    print("Unit Converter")
    print("Available conversions:")
    print("Length: meters, kilometers, centimeters, millimeters, inches, feet, yards, miles")
    print("Weight: grams, kilograms, milligrams, pounds, ounces")
    print("Temperature: celsius, fahrenheit, kelvin")
    
    conversion_type = input("Enter the type of conversion (length, weight, temperature): ").strip().lower()
    value = float(input("Enter the value to convert: "))
    from_unit = input("Enter the from unit: ").strip().lower()
    to_unit = input("Enter the to unit: ").strip().lower()
    
    if conversion_type == 'length':
        result = length_converter(value, from_unit, to_unit)
    elif conversion_type == 'weight':
        result = weight_converter(value, from_unit, to_unit)
    elif conversion_type == 'temperature':
        result = temperature_converter(value, from_unit, to_unit)
    else:
        print("Invalid conversion type.")
        return
    
    print(f"{value} {from_unit} is equal to {result} {to_unit}")

if __name__ == "__main__":
    main()
