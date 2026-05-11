# logical operators = evaluate multiple conditions (or, and, not)
#                     or = at least one condition must be true 
#                     and = both conditions must be true
#                     not = inverts the condition (not false, not true)


temp = 25
is_raining = True

if temp > 35 or temp < 0 or is_raining:
    print("The out door event is been canceled")
else:
    print("the outdoor event is still sheduled")


