# write a program that autoly prints the solution to the game, in which the rules are:

# 1. print each number from 1 to 100 in turn
# 2. when number is divisible by 3, istead of printing the number, print "Fizz"
# 3. when the number is divisible by 5, instead of printing the number, print "Buzz"
# 4. if the number is divisible by both 3 and 5, instead of printing the number, print "FizzBuzz"

for number in range(1, 101):
  if number%3 != 0 and number%5 != 0:
    print(number)
  elif number%3 == 0 and number%5 != 0:
    print("Fizz")
  elif number%3 != 0 and number%5 == 0:
    print("Buzz")
  else:
    print("FizzBuzz")

    