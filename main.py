
#  the task will be to get the program to print fizz if the number divides by 3,
#  print 5 if it divides by 5 and fizzbuzz to print when it divides by both

number = int(input("Please enter a number:\n"))
if number % 15 == 0:
    print("fizzbuzz")
elif number % 3 == 0:
    print("fizz")
elif number % 5 == 0:
    print("buzz")
else:
    print("Number does not divide by 3 or 5")
