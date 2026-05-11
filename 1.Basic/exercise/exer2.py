# Eersise 2 create shoppping cart program

print("Pruducts available list:")
print("pizza - $3.99")
print("cola - $1.99")
print("burger - $4.48")
print("chips - $1.00")
print("roll - $4.98")

rack = {
    "pizza": 3.99,
    "cola": 1.99,
    "burger": 4.48,
    "chips": 1.00,
    "roll": 4.98
}

print("\n")
print("-------------------------------------------")
item = input("what item would you like to eat?: ")
quantity = int(input("How many would you like?: "))
tip = float(input("Tip for our Service: "))

price = rack[item]
subtotal = price * quantity
total = subtotal + tip

print("\n\n")
print("-------------------------------")
print("Bill")
print("-------------------------------")
print(f"Product:    {item} x {quantity}")
print(f"subtotal:   ${subtotal}")
print(f"Tip:        ${tip}")
print("-------------------------------")
print(f"Final Total: ${total}")