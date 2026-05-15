

username = input("enter your username: ")

username.find(" ")

if len(username) > 12:
    print("your username cant be more than 12 charectors")
elif not username.find(" ") == -1:
    print(("username should not contain any spaces"))
elif not username.isalpha():
    print("username should not contain any digits")
else:
    print(f"welcome {username}")

