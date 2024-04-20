number = int(input("Please enter a number:\n"))
if number % 15 == 0:
    print("fizzbuzz")
elif number % 3 == 0:
    print("fizz")
elif number % 5 == 0:
    print("buzz")
else:
    print("Number does not divide by 3 or 5")
