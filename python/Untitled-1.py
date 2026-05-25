#QNO.1
# a=input("Enter a string: ")
# # print("Length of the string is: ",len(a))

# # #QNO.2
# l=float(input("Enter the length of the rectangle: "))
# b=float(input("Enter the breadth of the rectangle: "))
# area=l*b
# print("Area of the rectangle is: ",area)

# #QNO.3
# string = input("Enter a string: ")

# if len(string) < 2:
#     print("")
# else:
#     result = string[:2] + string[-2:]
#     print("Result:", result)

#QNO.3
# a= input("Enter a string: ")
# b=len(a)
# c=a[2]
# d=a[-2]
# if b<1:
#     print(c+a)
# else:
#     print("empty string")


# #QNO.4
# a= input("Enter a string: ")
# b=a[0]
# c=b+a[1:].replace(b, "#")
# print("Result: ",c)

# #QNO.5
# import math
# r=float(input("Enter the radius of the circle: "))
# area=math.pi*math.pow(r, 2)
# cir=2*math.pi*r
# print("Area of the circle is: ",area)
# print("Circumference of the circle is: ",cir)


#  #qno 6
# a=int(input("Enter a number: "))
# b=int(input("Enter another number: "))
# c=a+b
# print("The sum of the two numbers is: ",c)


# # #QNO.7
# import math
# a=int(input("Enter a number: "))
# b=math.sqrt(a)
# print("The square root of the number is: ",b)

# QNO.8 Area of a triangle
# a=float(input("Enter the base of the triangle: "))
# b=float(input("Enter the height of the triangle: "))
# area=0.5*a*b
# print("Area of the triangle is: ",area)     

#QNO.9 To find quadratic roots
# import math
# a = float(input("Enter the coefficient a: "))
# b = float(input("Enter the coefficient b: "))
# c = float(input("Enter the coefficient c: "))

# d = b**2 - 4*a*c

# if d > 0:
#     root1 = (-b + math.sqrt(d)) / (2*a)
#     root2 = (-b - math.sqrt(d)) / (2*a)
#     print("The roots are real and different.")
#     print("Root 1:", root1)
#     print("Root 2:", root2)

# if d == 0:
#     root = -b / (2*a)
#     print("The roots are real and equal.")
#     print("Root:", root)

# if d < 0:
#     real_part = -b / (2*a)
#     imaginary_part = math.sqrt(-d) / (2*a)
#     print("The roots are complex.")
#     print("Root 1:", real_part, "+", imaginary_part, "i")
#     print("Root 2:", real_part, "-", imaginary_part, "i")

#qno 9 
# import math

# a = float(input("Enter value of a: "))
# b = float(input("Enter value of b: "))
# c = float(input("Enter value of c: "))

# d = (b**2) - (4*a*c)

# root1 = (-b + math.sqrt(d)) / (2*a)
# root2 = (-b - math.sqrt(d)) / (2*a)

# print("Root 1 =", root1)
# print("Root 2 =", root2)
 
# # 10. Swap two variables

# a = input("Enter first value: ")
# b = input("Enter second value: ")

# print("Before swapping:")
# print("a =", a)
# print("b =", b)

# a, b = b, a

# print("After swapping:")
# print("a =", a)
# print("b =", b)

#  #qno 12. Find maximum of 2 numbers
# a = float(input("Enter first number: "))
# b = float(input("Enter second number: "))
# if a > b:
#     print("The maximum number is:", a)
# elif b > a:
#     print("The maximum number is:", b)
# else:    print("Both numbers are equal.")


#class work 

#1
# count=0
# while count < 5:
#     count += 1
#     print("iteration no. {}".format(count))
# print("end of while loop")












#LAB 1: PYTHON BASICS
#Print all the even numbers from 0 to 10.
# for i in range(0, 11):
#     if i % 2 == 0:
#         print(i)
 
# QNO 2: Add logic to print two lines. The first line should contain the result of integer division, //. The second line should contain the result of float division, /.
# a = 10
# b = 3
# print("Integer division (//):", a // b)
# print("Float division (/):", a / b)

#Evaluate following the expression a. 4 * (6 + 5)
# result = 4 * (6 + 5)
# print("Result of 4 * (6 + 5):", result)

#Evaluate following the expression b. 4 * 6 + 5
# result = 4 * 6 + 5
# print("Result of 4 * 6 + 5:", result)

# # c. (5 > 4) and (3 == 5)  
# result = (5 > 4) or (3 == 5)
# print("Result of (5 > 4) or (3 == 5):", result)
 
#  #d. not (5 > 4)
# result = not (5 > 4)
# print("Result of not (5 > 4):", result)

#e. 4 + 6 * 5
# result = 4 + 6 * 5
# print("Result of 4 + 6 * 5:", result) 

#f. not ((5 > 4) or (3 == 5)
# result = not ((5 > 4) or (3 == 5))
# print("Result of not ((5 > 4) or (3 == 5)):", result)

#g. (True and True) and (True == False
# result = (True and True) and (True == False)
# print("Result of (True and True) and (True == False):", result)   

#i.(not False) or (not True)
# result = (not False) or (not True)
# print("Result of (not False) or (not True):", result)

#4. What is the type of the result of the expression 3* 1.5 +4
# result = 3 * 1.5 + 4
# print("Result of 3 * 1.5 + 4:", result)
# print("Type of the result:", type(result))  

#5. Find a number’s square root as well as square 
# import math
# num = float(input("Enter a number: "))
# square_root = math.sqrt(num)
# square = num ** 2
# print("Square root of", num, "is:", square_root)
# print("Square of", num, "is:", square)

#6. Find the area of a triangle with base 10 and height 5
# base = 10
# height = 5
# area = 0.5 * base * height
# print("Area of the triangle is:", area)

#7. Write a Python program to test if a variable is a list, tuple, or set.
# my_variable = [1, 2, 3]
# if isinstance(my_variable, list):
#     print("The variable is a list.")
# elif isinstance(my_variable, tuple):
#     print("The variable is a tuple.")
# elif isinstance(my_variable, set):
#     print("The variable is a set.")
# else:
#     print("The variable is not a list, tuple, or set.")

# 8. Write a Python program to print the following string in a specific format.Output :
# Twinkle, twinkle, little star,
# How I wonder what you are!
# Up above the world so high,
# Like a diamond in the sky.
# Twinkle, twinkle, little star,
# How I wonder what you are


# print("Twinkle, twinkle, little star,\nHow I wonder what you are!\nUp above the world so high,\nLike a diamond in the sky.\nTwinkle, twinkle, little star,\nHow I wonder what you are")


#9. Write a Python program to find out what version of Python you are using.
#import sys
# print("Python version:", sys.version)

#10. Write a Python program to display the first and last colors from the following list. color_list = ["Red", "Green", "White", "Black", “Blue”]
# color_list = ["Red", "Green", "White", "Black", "Blue"]
# print("First color:", color_list[0])
# print("Last color:", color_list[-1])

#11.Write a Python program to get the volume of a sphere with radius=6.
# import math 
# radius = 6
# volume = (4/3) * math.pi * radius**3
# print("Volume of the sphere:", volume)

#12. Write a Python program to calculate the sum of three given numbers. If the values are equal, return three times their sum
# num1 = float(input("Enter first number: "))
# num2 = float(input("Enter second number: "))
# num3 = float(input("Enter third number: "))
# if num1 == num2 == num3:
#     result = 3 * (num1 + num2 + num3)
# else:
#     result = num1 + num2 + num3
# print("Result:", result)


#13. Write a Python program to sum two given integers. However, if the sum is between 15 and 20 it will return 20
# num1 = int(input("Enter first integer: "))
# num2 = int(input("Enter second integer: "))
# sum = num1 + num2
# if 15 <= sum <= 20:
#     print("Result:", 20)
# else:
#     print("Result:", sum)

#14. 14. Write a Python program that displays your name, age, and address on three different lines.
# name = "Simrika Chaulagain"
# age = 30
# address = "Bhaktapur, Nepal"
# print("Name:", name)
# print("Age:", age)
# print("Address:", address)    

#15. Write a Python program to solve (x + y) * (x + y)
# x = float(input("Enter value of x: "))
# y = float(input("Enter value of y: "))
# result = (x + y) * (x + y)
# print("Result of (x + y) * (x + y):", result) 

#16.Write a Python program to concatenate N strings.
# N = int(input("Enter the number of strings to concatenate: "))
# strings = []
# for i in range(N):
#     string = input("Enter string {}: ".format(i + 1))
#     strings.append(string)
# result = "".join(strings)
# print("Concatenated string:", result)
#17. Given variables x=30 and y=20, write a Python program to print "30+20=50".
# x = 30
# y = 20
# result = x + y
# print(x, "+", y, "=", result)

# 18.Print different type of variables i.e. determine the type of an object/ a variable in Python.
# x = 10
# y = 3.14
# z = "Hello, World!"
# print("Value of x:", x, "Type of x:", type(x))
# print("Value of y:", y, "Type of y:", type(y))
# print("Value of z:", z, "Type of z:", type(z))

# #19. Write a Python program to ask the user to input their name, stores it in the variable “name”, and thenprints a greeting message addressing the user by their entered name.Use input() function
# name = input("Please enter your name: ")
# print("Hello, " + name + "! Welcome to Python programming.")

#20. Write a Python program to ask the user to input an integer representing the number of roses, converts the input to an integer using typecasting, and then prints the integer value.

# roses = input("Enter the number of roses: ")
# # Convert the input to an integer using typecasting
# roses = int(roses)

# print("Number of roses:", roses)

