
# sum=0
# n=int(input("Enter a number: "))
# while n!=0:
#     sum+=n
#     n=int(input("Enter a number: "))
# print("The sum of the numbers is: ",sum)

#qno 2 
# i=0
# while i<4:
#     i+=1
#     if i%2==0:
#         print(i)
#         break
#     else: 
#         print("no break")

#qno 3
# i=2
# while i<6:
#     print(i)
#     i+=1
# else:
#     print("i is no longer less than 6")

#qno1:  Wap to enter a character from user and check if it is vowel or consonant
# char=input("Enter a character: ")
# if char in 'aeiouAEIOU':
#     print("The character is a vowel.")    
# else:
#     print("The character is a consonant.")

#qno2: WAP to enter a num from user and print its absolute value 
# num=float(input("Enter a number: "))
# if num < 0:
#     num = -num
# print("The absolute value of the number is: ", num)
 
#wap to print following series: 1 4 9 16 36 49 64 81 100.. N
# n=int(input("Enter a number: "))
# for i in range(1, n+1):
#     print(i**2, end=' ')


# wap to print following series: 1/1 2/4 3/9 4/16 5/25 6/36 7/49 8/64 9/81 10/100.. N
# n=int(input("Enter a number: "))
# for i in range(1, n+1):
#     print(f"{i}/{i**2}", end=' ')

#wap to enter a number from user and reverse the number and print it
# num=int(input("Enter a number: "))
# reversed_num=0
# while num>0:
#     digit=num%10
#     reversed_num=reversed_num*10+digit
#     num=num//10
# print("The reversed number is: ",reversed_num)
 
#wap to enter a number from user and print sum of its individual digits 
# num=int(input("Enter a number: "))
# sum=0
# while num>0:
#     digit=num%10
#     sum+=digit
#     num=num//10
# print("The sum of the digits is: ",sum)

# wap to enter a number from user and check if it is palindrome or not
# num=int(input("Enter a number: "))
# original_num=num
# reversed_num=0
# while num>0:
#     digit=num%10
#     reversed_num=reversed_num*10+digit
#     num=num//10
# if original_num==reversed_num:
#     print("The number is a palindrome.")
# else:
#     print("The number is not a palindrome.")

#wap to enter a number from user and print its individual digits in separate line  in order
# num=int(input("Enter a number: "))
# for digit in str(num):
#     print(digit)

# num = input("Enter number: ")

# for i in num:
#     print(i)

#wap to enter a number from user and print factorial of it 
# num=int(input("Enter a number: "))
# factorial=1
# for i in range(1, num+1):
#     factorial*=i
# print("The factorial of the number is: ",factorial)

# #wap to enter a number from user and print its multiplication table
# num=int(input("Enter a number: "))
# for i in range(1, 11):
#     print(f"{num} x {i} = {num*i}")

#wap to enter a limit from user and print fibonacci series up to that limit
# range=int(input("Enter a range: "))
# a, b = 0, 1
# while a < range:
#     print(a, end=" ")
#     a, b = b, a + b  


# range = int(input("Enter a range: "))
# a, b = 0, 1
# while a < range:
#     print(a, end=" ")
#     a, b = b, a + b

#print patter 
# for i in range(1, 6):
#     print("*" * i)

# #1
# #22
# #333
# #4444
# #55555

# for i in range(1, 6):
#     for j in range(1, i+1):
#         print(i, end=" ")
#     print()

# #5
# #44
# #333
# #2222
# #11111
# for i in range(5, 0, -1):
#     for j in range(1, i+1):
#         print(i, end=" ")
#     print()

# *****
# *****
# *****
# *****
# *****
# for i in range(5):
#     for j in range(5):
#         print("*", end=" ")
#     print()
