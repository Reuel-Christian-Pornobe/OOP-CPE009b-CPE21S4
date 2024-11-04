"""
@author: Pornobe, Reuel Christian, M.
"""

# adding two conversion methods - Fahrenheit to Celsius and Kelvin to Celsius

def main():
    class TemperatureConversion:
        def __init__(self, temp=1):
            self._temp = temp
        
    class CelsiusToFahrenheit(TemperatureConversion):
        def conversion(self):
            return (self._temp * 9) / 5 + 32
        
    class CelsiusToKelvin(TemperatureConversion):
        def conversion(self):
            return self._temp + 273.15
        
    class KelvinToCelsius(TemperatureConversion):           # Kelvin To Celsius
        def conversion(self):
            return self._temp - 273.15
        
    class FahrenheitToCelsius(TemperatureConversion):       # Fahrenheit to Celsius
        def conversion(self):
            return (self._temp - 32) * (5/9)
        
    class FahrenheitToKelvin(TemperatureConversion):        # Fahrenheit to Kelvin
        def conversion(self):
            return ((self._temp - 32) * (5/9)) + 273.15        
    
    
    # Conversion of Celsius to Fahrenheit and Kelvin
    tempInCelsius = float(input("Enter the temperature in Celsius: "))   
    convert = CelsiusToKelvin(tempInCelsius)
    print(str(convert.conversion()) + " Kelvin")
    convert = CelsiusToFahrenheit(tempInCelsius)
    print(str(convert.conversion()) + " Fahrenheit")
    
    # Conversion of Fahrenheit to Celsius and Kelvin
    tempInFahrenheit = float(input("Enter the temperature in Fahrenheit: "))
    convert = FahrenheitToKelvin(tempInFahrenheit)
    print(str(convert.conversion()) + " Kelvin")
    convert = FahrenheitToCelsius(tempInFahrenheit)
    print(str(convert.conversion()) + " Celsius")
     
    # Conversion of Kelvin to Celsius
    tempInKelvin = float(input("Enter the temperature in Kelvin: "))
    convert = KelvinToCelsius(tempInKelvin)
    print(str(convert.conversion()) + " Celsius")



main()
