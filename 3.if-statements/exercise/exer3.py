# temperature conversion program

unit = input("Is this temprature in celsius or farenheight (c/f): ")
temp = float(input("Enter the temperature: "))

if unit == "c":
    temp = (9 * temp) / 5 + 32
    unit = "°F"
    print(f"temperature is {round(temp, 2)} {unit}")
elif unit == "C":
    temp = (9 * temp) / 5 + 32
    unit = "°F"
    print(f"temperature is {round(temp, 2)} {unit}")
elif unit == "f":
    temp = (5 * (temp - 32)) / 9
    unit = "°C"
    print(f"temperature is {round(temp, 2)} {unit}")
elif unit == "F":
    temp = (5 * (temp - 32)) / 9
    unit = "°C"
    print(f"temperature is: {round(temp, 2)} {unit}")
else:
    print(f"{unit} is not valid unit")