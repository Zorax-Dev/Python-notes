# while loop = execute some code while some condition remains true

food = input("enter a food you liked (q to quit): ")

while not food == "q":
    print(f"you like {food}")
    food = input("enter another food you liked (q to quit): ")

print("bye")