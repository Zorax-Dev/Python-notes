# Python weight converter 

weight = float(input("Enter your weight: "))
unit = input("kilograms or pounds? (k or L): ")

if unit == "k":
    weight = weight * 2.205
    unit = "Lbs." 
    print(f"approximate conversion: {round(weight, 3)} {unit}")
elif unit == "l":
    weight = weight / 2.205
    unit = "Kg."
    print(f"approximate conversion: {round(weight, 3)} {unit}") 
elif unit == "K":
    weight = weight * 2.205 
    unit = "Lbs."
    print(f"approximate conversion: {round(weight, 3)} {unit}") 
elif unit == "L":
    weight = weight / 2.205
    unit = "Kg." 
    print(f"approximate conversion: {round(weight, 3)} {unit}")
else: 
    print(f"{unit} was not valid unit")

