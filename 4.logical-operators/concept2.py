# logical operators = evaluate multiple conditions (or, and, not)
#                     or = at least one condition must be true 
#                     and = both conditions must be true
#                     not = inverts the condition (not false, not true)


temp = 20
is_sunny = False

if temp >= 28 and is_sunny:
    print("It is hot outside 🥵")
    print("It is sunny ☀️")
elif temp <= 0 and is_sunny:
    print("It is cold outside 🥶")
    print("ity is sunny ☀️")
elif 28 > temp > 0 and is_sunny:
    print("It is warm outside 🥵")
    print("ity is sunny ☀️")
elif temp >= 28 and not is_sunny:
    print("It is hot outside 🥵")
    print("it is cloudy ☁️")
elif temp <= 0 and not is_sunny:
    print("It is cold outside 🥶")
    print("ity is cloudy ☁️")
elif 28 > temp > 0 and not is_sunny:
    print("It is warm outside 🥵")
    print("ity is cloudy ☁️")