"""
    Python Code Challenges: Functions

"""

""" 
    1. Tenth Power

    Write a function named tenth_power() that has one parameter named num.

    The function should return num raised to the 10th power.
"""

# Write your tenth_power function here:
def tenth_power(num):
  return num ** 10


print(" 1. Tenth Power")

print(tenth_power(1))
# 1 to the 10th power is 1
print(tenth_power(0))
# 0 to the 10th power is 0
print(tenth_power(2))
# 2 to the 10th power is 1024

"""
    2. Square Root

    Write a function named square_root() that has one parameter named num.

    Use exponents (**) to return the square root of num.
"""

# Write your square_root function here:
def square_root(num):
  return num ** 0.5

print(" 2. Square Root")

print(square_root(16))
# should print 4
print(square_root(100))
# should print 10



"""
    3. Win Percentage

    Create a function called win_percentage() that takes two parameters named wins and losses.

    This function should return out the total percentage of games won by a team based on these two numbers.
"""

# Write your win_percentage function here:
def win_percentage(wins, losses):
  total_games = wins + losses
  ratio_won = wins / total_games
  return ratio_won * 100

print(" 3. Win Percentage")

# Uncomment these function calls to test your win_percentage function:
print(win_percentage(5, 5))
# should print 50
print(win_percentage(10, 0))
# should print 100


"""
4. Average

Write a function named average() that has two parameters named num1 and num2.

The function should return the average of these two numbers.
"""

# Write your average function here:
def average(num1, num2):
  return (num1 + num2) / 2

print(" 4. Average")

# Uncomment these function calls to test your average function:
print(average(1, 100))
# The average of 1 and 100 is 50.5
print(average(1, -1))
# The average of 1 and -1 is 0


"""
5. Remainder

Write a function named remainder() that has two parameters named num1 and num2.

The function should return the remainder of twice num1 divided by half of num2.
"""

# Write your remainder function here:
def remainder(num1, num2):
  numerator = num1 * 2
  denominator = num2 / 2
  return numerator % denominator


# SOLUTION #2 
def remainder(num1, num2):
  return (2 * num1) % (num2 / 2)

print(" 5. Reminder")

# Uncomment these function calls to test your remainder function:
print(remainder(15, 14))
# should print 2
print(remainder(9, 6))
# should print 0



"""________________Python Code Challenges: Functions (Advanced)_______________________"""

"""
    1. First Three Multiples

    Write a function named first_three_multiples() that has one parameter named num.

    This function should print the first three multiples of num. Then, it should return the third multiple.

    For example, first_three_multiples(7) should print 7, 14, and 21 on three different lines, and return 21.
"""

# Write your first_three_multiples function here
def first_three_multiples(num):
  for number in range(1,4):
    print(num * number)
  return num * 3

# SOLUTION #2
def first_three_multiples_2(num):
  print(num)
  print(num * 2)
  print(num * 3)
  return num * 3

print(" 1. First Three Multiples")

first_three_multiples(10)
# should print 10, 20, 30, and return 30
first_three_multiples(0)
# should print 0, 0, 0, and return 0


"""
    2. Tip

    Create a function called tip() that has two parameters named total and percentage.

    This function should return the amount you should tip given a total and the percentage you want to tip.
"""

# Write your tip function here:
def tip(total,percentage):
  return (total * percentage) / 100

#SOLUTION #2
def tip_2(total, percentage):
  tip_amount = (total * percentage) / 100
  return tip_amount

print(" 2. Tip")

print(tip(10, 25))
# should print 2.5
print(tip(0, 100))
# should print 0.0

"""
    3. Bond, James Bond

    Write a function named introduction() that has two parameters named first_name and last_name.

    The function should return the last_name, followed by a comma, a space, first_name another space, and finally last_name.
"""

# Write your introduction function here:
def introduction(first_name, last_name):
  return last_name + ", " + first_name + " " + last_name

#SOLUTION #2 usinf f format {}
def introduction_2(first_name, last_name):
  return (f"{last_name}, {first_name} {last_name}")


print("   3. Bond, James Bond")

print(introduction_2("James", "Bond"))
# should print Bond, James Bond
print(introduction("Maya", "Angelou"))
# should print Angelou, Maya Angelou

"""
    4. Dog Years

    Some say that every one year of a human’s life is equivalent to seven years of a dog’s life. 
    Write a function named dog_years() that has two parameters named name and age.

    The function should compute the age in dog years and return the following string:
    "{name}, you are {age} years old in dog years"
"""
# Write your dog_years function here:
def dog_years(name, age):
  return f"{name}, you are {age*7} years old in dog years"

#SOLUTION #2
def dog_years_2(name, age):
  return name+", you are "+str(age * 7)+" years old in dog years"

# Uncomment these function calls to test your dog_years function:
print(dog_years("Lola", 16))
# should print "Lola, you are 112 years old in dog years"
print(dog_years("Baby", 0))
# should print "Baby, you are 0 years old in dog years"

"""
    5. All Operations

    Create a function named lots_of_math(). This function should have four parameters named a, b, c, and d. 
    The function should print 3 lines and return 1 value.

    First, print the sum of a and b.

    Second, print c minus d.

    Third, print the first number printed, 
    multiplied by the second number printed.

    Finally, return the third number printed modulo a.
"""

# Write your lots_of_math function here:
def lots_of_math(a, b, c, d):
  print(a + b) 
  print(c - d) 
  print((a + b) * (c - d)) 
  return ((a + b) * (c - d)) % a 

#SOLUTION #2
def lots_of_math_2(a, b, c, d):
  first = a + b
  second = c - d
  third = first * second
  fourth = third % a
  print(first)
  print(second)
  print(third)
  return fourth


# Uncomment these function calls to test your lots_of_math function:
print(lots_of_math(1, 2, 3, 4))
# should print 3, -1, -3, 0
print(lots_of_math_2(1, 1, 1, 1))
# should print 2, 0, 0, 0