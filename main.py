# Temperature conversion program

unit = input("Which temp C° or °F? (C/F): ")
temp = float(input("Enter your temp here: "))

if unit == "C":
    temp = round((temp * 9) / 5 + 32, 2)
    unit = "°F"
    print(f"The temp in °F is: {temp}{unit}")
elif unit == "F":
    temp = round((temp - 32) * 5 / 9, 2)
    unit = "C°"
    print(f"The temp in C° is: {temp}{unit}")
else:
    print("Sorry your input an invalide, Try agin!")