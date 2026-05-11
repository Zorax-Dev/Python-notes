# if = Do some code only if some conndition is true 
#      else do something else

age = int(input("enter your age: "))

if age >= 100:
    print("your too old to sign up!")
elif age >= 18:
    print("You are signed up!")
elif age < 0:
    print("you havent been born yet!")
else:
    print("You must be 18+ to sign up")