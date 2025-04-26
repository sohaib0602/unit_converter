import streamlit as st

# Function to convert units
def convert_units(value, from_unit, to_unit):
    # Define conversion factors
    conversion_factors = {
        'length': {
            'meters': 1,
            'kilometers': 0.001,
            'miles': 0.000621371,
            'feet': 3.28084,
            'inches': 39.3701
        },
        'weight': {
            'grams': 1,
            'kilograms': 0.001,
            'pounds': 0.00220462,
            'ounces': 0.035274
        },
        'temperature': {
            'celsius': lambda x: x,
            'fahrenheit': lambda x: (x * 9/5) + 32,
            'kelvin': lambda x: x + 273.15
        }
    }

    # Check the type of conversion
    if from_unit in conversion_factors['length'] and to_unit in conversion_factors['length']:
        return value * conversion_factors['length'][to_unit] / conversion_factors['length'][from_unit]
    elif from_unit in conversion_factors['weight'] and to_unit in conversion_factors['weight']:
        return value * conversion_factors['weight'][to_unit] / conversion_factors['weight'][from_unit]
    elif from_unit in conversion_factors['temperature'] and to_unit in conversion_factors['temperature']:
        if from_unit == 'celsius' and to_unit == 'fahrenheit':
            return conversion_factors['temperature']['fahrenheit'](value)
        elif from_unit == 'fahrenheit' and to_unit == 'celsius':
            return (value - 32) * 5/9
        elif from_unit == 'celsius' and to_unit == 'kelvin':
            return conversion_factors['temperature']['kelvin'](value)
        elif from_unit == 'kelvin' and to_unit == 'celsius':
            return value - 273.15
        elif from_unit == 'fahrenheit' and to_unit == 'kelvin':
            return conversion_factors['temperature']['kelvin']((value - 32) * 5/9)
        elif from_unit == 'kelvin' and to_unit == 'fahrenheit':
            return conversion_factors['temperature']['fahrenheit'](value - 273.15)
    else:
        return None

# Streamlit app
st.title("Unit Converter")

# Select conversion type
conversion_type = st.selectbox("Select conversion type", ["Length", "Weight", "Temperature"])

# Input value
value = st.number_input("Enter value", min_value=0.0)

# Select units based on conversion type
if conversion_type == "Length":
    from_unit = st.selectbox("From unit", ["meters", "kilometers", "miles", "feet", "inches"])
    to_unit = st.selectbox("To unit", ["meters", "kilometers", "miles", "feet", "inches"])
elif conversion_type == "Weight":
    from_unit = st.selectbox("From unit", ["grams", "kilograms", "pounds", "ounces"])
    to_unit = st.selectbox("To unit", ["grams", "kilograms", "pounds", "ounces"])
else:  # Temperature
    from_unit = st.selectbox("From unit", ["celsius", "fahrenheit", "kelvin"])
    to_unit = st.selectbox("To unit", ["celsius", "fahrenheit", "kelvin"])

# Convert and display result
if st.button("Convert"):
    result = convert_units(value, from_unit, to_unit)
    if result is not None:
        st.success(f"{value} {from_unit} = {result:.4f} {to_unit}")
    else:
        st.error("Conversion not possible.")