# Write a program that prints the numbers from 1 to 100.
# But for multiples of three print “Fizz” instead of the number
# and for the multiples of five print “Buzz”.
# For numbers which are multiples of both three and five print “FizzBuzz”.

for x in range(1,101):
    if x % 5 == 00 and x % 3 == 00:
        x = "FizzBuzz"
    elif x % 3 == 00:
        x = "Fizz"
    elif x % 5 == 00:
        x = "Buzz"
    print(x)
