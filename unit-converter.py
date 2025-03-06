import streamlit as st

# Function to convert units
def convert_unit(value, unit_from, unit_to):
    # Dictionary containing conversion factors
    conversions = {
        # Length Conversions
        "meters_kilometers": 0.001,
        "kilometers_meters": 1000,
        "meters_centimeters": 100,
        "centimeters_meters": 0.01,
        "inches_centimeters": 2.54,
        "centimeters_inches": 0.393701,
        "miles_kilometers": 1.60934,
        "kilometers_miles": 0.621371,

        # Weight Conversions
        "grams_kilograms": 0.001,
        "kilograms_grams": 1000,
        "pounds_kilograms": 0.453592,
        "kilograms_pounds": 2.20462,
        "ounces_grams": 28.3495,
        "grams_ounces": 0.035274,

        # Time Conversions
        "seconds_minutes": 1/60,
        "minutes_seconds": 60,
        "minutes_hours": 1/60,
        "hours_minutes": 60,
    }
    
    # Special case for temperature conversion
    if unit_from == "Celsius" and unit_to == "Fahrenheit":
        return (value * 9/5) + 32  # °C to °F formula
    elif unit_from == "Fahrenheit" and unit_to == "Celsius":
        return (value - 32) * 5/9  # °F to °C formula

    # Create a key for conversion lookup
    key = f"{unit_from}_{unit_to}"  
    
    # Check if the conversion exists in the dictionary
    if key in conversions:
        return value * conversions[key]  # Perform conversion
    else:
        return None  # Return None if conversion is not supported

# Streamlit App Title
st.title("Advanced Unit Converter")

# User input for numerical value
value = st.number_input(
    "Enter your value:", 
    min_value=0.0,  # Prevents negative inputs
    step=0.1,       # Allows floating-point input
    format="%.2f"   # Displays value with 2 decimal places
)

# Dropdowns to select units for conversion
unit_options = [
    "meters", "kilometers", "centimeters", "inches", "miles",
    "grams", "kilograms", "pounds", "ounces",
    "seconds", "minutes", "hours",
    "Celsius", "Fahrenheit"
]

unit_from = st.selectbox("Convert from:", unit_options)
unit_to = st.selectbox("Convert to:", unit_options)

# Convert button
if st.button("Convert"):
    result = convert_unit(value, unit_from, unit_to)  # Call conversion function
    
    # Display result if conversion is valid
    if result is not None:
        st.success(f"Converted Value: {result:.2f} {unit_to}")  # Display result with 2 decimal places
    else:
        st.error("Conversion not supported between these units!")  # Show error for unsupported conversions
