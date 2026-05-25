# # 1. Write a Python program to calculate the difference between a given number and 17. If the number is greater than 17, return twice the absolute difference.
# number = int(input("Enter a number: "))
# difference = abs(number - 17)
# if number > 17:
#     result = 2 * difference
# else:
#     result = difference
# print("Result:", result)

# #2. Write a Python program that determines whether a given number (accepted from the user) is even or odd, and prints an appropriate message to the user.even or odd, and prints an appropriate message to the user
# number = int(input("Enter a number: "))
# if number % 2 == 0:
#     print("The number is even.")
# else:    
#     print("The number is odd.")

# 3. Write a Python program to count the number of 4s in a list.
# list = [1, 4, 6, 4, 7, 4, 9]
# count = 0
# for num in list:
#     if num == 4:
#         count += 1
# print("Number of 4s in the list:", count)

#4. Write a Python program to swap two variables.
# a = 5
# b = 10
# print("Before swapping: a =", a, "b =", b)
# a, b = b, a
# print("After swapping: a =", a, "b =", b)

# #5. Write a Python program to check whether a variable is an integer, or string, or a list, or tuple, or set
# variable = input("Enter a variable: ")
# if variable.isdigit():
#     print("The variable is an integer.")
# elif variable.startswith("[") and variable.endswith("]"):
#     print("The variable is a list.")
# elif variable.startswith("(") and variable.endswith(")"):
#     print("The variable is a tuple.")
# elif variable.startswith("{") and variable.endswith("}"):
#     print("The variable is a set.")
# else:
#     print("The variable is a string.")

#6. Write a Python script that takes two numbers as input and prints their sum, difference, product, and quotient
# num1=float(input("enter number 1: "))
# num2=float(input("enter number 2: "))
# sum=num1+num2
# difference = num1-num2
# product = num1*num2
# quotient = num1/num2
# print("Sum is: ",sum)
# print("Difference is: ",difference)
# print("Product is: ",product)
# print("Quotient is: ",quotient)

#7. Take an input from user then reverse the string using slicing.
# string = input("Enter a string: ")
# reversed_string = string[::-1]
# print("Reversed string:", reversed_string)

#8. Write code to take input from user and store it in a variable spam then print Hello if 1 is storedin spam, print Hi if 2 is stored in spam, and print Greetings! if anything else is stored in spam.
# spam = int(input("Enter a number: "))
# if spam == 1:
#     print("Hello")
# elif spam == 2:
#     print("Hi")
# else:
#     print("Greetings!")

#9. Write a Python script that takes two numbers as input and prints their sum, difference, product, and quotient using match case.and quotient using match case.
# num1 = float(input("Enter number 1: "))
# num2 = float(input("Enter number 2: "))
# operation = input("Enter the operation (sum, difference, product, quotient): ")
# match operation:
#     case "sum":
#         result = num1 + num2
#         print("Sum is:", result)
#     case "difference":
#         result = num1 - num2
#         print("Difference is:", result)
#     case "product":
#         result = num1 * num2
#         print("Product is:", result)
#     case "quotient":
#         if num2 != 0:
#             result = num1 / num2
#             print("Quotient is:", result)
#         else:
#             print("Error: Division by zero is not allowed.")
#     case _:
#         print("Invalid operation. Please choose from sum, difference, product, or quotient.")

#10.  Write a script that asks the user for their name and age, then prints a message that tells them the year in which they will turn 100 years old.

# from datetime import datetime
# name=input("Enter your name: ")
# age=int(input("Enter your age:"))
# current_year = datetime.now().year
# year_turn_100 = current_year + (100 - age)
# diff=100-age
# print("you will turn 100 in next", diff, "years!")
# print("You will turn 100 in the year", year_turn_100)

 #11. Create a Python script that converts temperature from Fahrenheit to Celsius and vice versa, based on user input
# temp = float(input("Enter the temperature: "))
# unit = input("Enter the unit (F for Fahrenheit, C for Celsius): ").upper()
# if unit == "F":
#     celsius = (temp - 32) * 5.0/9.0
#     print(f"{temp}°F is equal to {celsius:.2f}°C")
# elif unit == "C":
#     fahrenheit = (temp * 9.0/5.0) + 32
#     print(f"{temp}°C is equal to {fahrenheit:.2f}°F")
# else:
#     print("Invalid unit. Please enter 'F' for Fahrenheit or 'C' for Celsius.")


#12. Create a program that asks for an age and prints “Child” if the age is less than 12, “Teenager” if the age is between 13 and 19, and “Adult” for ages 20 and above
# age = int(input("Enter your age: "))
# if age<=12: 
#     print("child")
# elif 13<=age<=19:
#     print("teenager")
# elif 20<=age<34:
#     print("adult")
# else:
#     print("aged")

#13.  Write a python script that takes a letter grade (A, B, C, D, F) as input and prints the corresponding grade point average (GPA). For example, A = 4.0, B = 3.0, C = 2.0, D = 1.0, F=0.0. Include an else statement to handle invalid inputs

# grade=input("enter your grade(A,B,C,D,F):").upper()
# if grade=='A': 
#     print("Congratulationa! You have got 4.00 GPA! ")
# elif grade=='B':
#     print("You have got 3.00 GPA!")
# elif grade=='C':
#     print("You have got 2.00 GPA!")
# elif grade=='D':
#     print("You have got 1.00 GPA!")
# elif grade=='F':
#     print("0.00")
# else:
#     print("Invalid input.") 

#14.Write a python program that takes a number and prints whether it is “Even”, “Odd”, “Zero”, or “Invalid” for non-integer inputs. This program should first check if the input is a valid integer“Invalid” for non-integer inputs. This program should first check if the input is a valid integer and then check for the other conditions.
# try:
#     n = int(input("Enter a number: "))
#     print("Valid integer")
#     if n % 2 == 0:
#         print("Even")
#     elif n == 0:
#         print("zero")
#     else: 
#         print("odd")
# except:
#     print("Not a valid integer")
# # 15
# year = int(input("Enter a year: "))
# result = (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0)
# print(result)



#class 2: 

# #wap to print pattern: 
# #*
# #**
# #***
# #****
# #*****
# for i in range(1,6):
#     print("*" * i)


# #star pattern (square)
# for i in range(5):
#     print("*" * 5)



# for i in range(1,6):
#     for j in range(1,i+1):
#         print(j, end="")
#     print()    


# for i in range(1,6):
#     print(str(i)*i)

# for i in range(6,0,-1):
#     print(str(i)*(6-i))

#reverse number pattern 
# for i in range(1,6):
#     for j in range(i,0,-1):
#         print(j, end="")
#     print()



#reverse number pattern 
#5
#54
#543
#5432
# #54321
# for i in range(1,6):
#     for j in range(5,5-i,-1):
#         print(j, end="")
#     print()

for i in range(5,0,-1):
    for j in range(5,5-i,-1):
        print(j, end="")
    print()