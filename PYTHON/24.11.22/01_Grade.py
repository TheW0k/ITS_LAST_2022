"""
# Conversioni di temperature
#
# @author: TheW0k
# @version 1.0 2022-11-24
"""
temp_in = int(input("Temperatura: "))
input = input("Input (c, k, f): ")
out = input("Scala in output (c, k, f): ")

if input == "C" or input == "c":
    if out == "F" or out == "f":
        temperatura_out = temp_in * 1.8 + 32
    else:
        temperatura_out = temp_in + 273.15  # Kelvin
elif input == "F" or input == "f":
    if out == "C" or out == "c":
        temperatura_out = (temp_in - 32) / 1.8
    else:
        temperatura_out = (temp_in - 32) / 1.8 + 273.15  # Kelvin
else:
    if out == "C" or out == "c":
        temperatura_out = temp_in - 273.15
    else:
        temperatura_out = (temp_in - 273.15) * 1.8 + 32  # Fahrenheit
    
print("Temperatura: ", temperatura_out, " °", out, sep="")