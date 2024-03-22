# 1. In a town, the percentage of men is 52. The percentage of total literacy is 48. If total percentage of literate men is 35 of the total population, write a program to find the total number of illiterate men and women if the population of the town is 80,000.

 
population =80000
men = population*(52/100)
men1= men*(35/100)
women=population*((100-52)/100)
women1=women*((48-35)/100)
a=men1+ women1
print(x)

# 2.A cashier has currency notes of denominations 10, 50 and 100. If the amount to be withdrawn is input through the keyboard in hundreds, find the total number of currency notes of each denomination the cashier will have to give to the withdrawer
  
   withdraw_amount=int(input())
   a=withdraw_amount//100
   a1=withdraw_amount%100
   b=a1//50
   b1=a1%50
   c=b1//10
   print("Hundreds",a)
   print("fifty",b)
   print("ten",c)
                
# 3.While purchasing certain items, a discount of 10% is offered if the quantity purchased is more than 10. If quantity and price per item are input through the keyboard, write a program to calculate the total expenses.

quantity=int(input())
if(quantity>10):
    a=0
    b=0
    for i in range(quantity):
        amount=int(input())
        a=amount+a
        b=a*(10/100)
        c=a-b
        print(n)
else:
    y=0
    for j in range(quantity):
        expenses=int(input())
        y=expenses+y
    print(y)



 
#     4.If his basic salary is less than Rs. 1500, then HRA = 10% of basic salary and DA = 90% of basic salary. If his salary is either equal to or above Rs. 1500, then HRA = Rs. 500 and DA = 98% of basic salary. If the employee's salary is input through the keyboard write a program to find his gross salary
n = int(input("Employee's Salary :"))
if n<1500:
    hra = n/10
    da = (n/100)*90
else:
    hra = 500
    da = (n/100)*98
    gross_salary = n+hra+da
    print("Gross Salary : ",gross_salary)

   
   
# 5. If the ages of Ram, Shyam and Ajay are input through the keyboard, write a program to determine the youngest of the three.  
a = int(input("Enter the age of Ram : "))
b = int(input("Enter the age of Shyam : "))
c = int(input("Enter the age of Ajay : "))

if a<b and a<c:
	print("Ram is the youngest of the three")
	
elif b<a and b<c:
	print("Shyam is the youngest of the three")

else:
	print("Ajay is the youngest of the three")

# 6.Any year is entered through the keyboard, write a program to determine whether the year is leap or not. Use the logical operators && and ||.


year = int(input("Enter a Year : "))
if (year % 400 == 0 ) or (year % 4 == 0  and  year % 100 != 0) :
    print(year, " is a leap year")
else :
    print(year, " is not a leap year")


# 7.A library charges a fine for every book returned late. For first 5 days the fine is 50 paise, for 6-10 days fine is one rupee and above 10 days fine is 5 rupees. If you return the book after 30 days your membership will be cancelled. Write a program to accept the number of days the member is late to return the book and display the fine or the appropriate message.
if days <= 5 :
    fine_amount = days * 0.5
    print("Fine Amount : ",fine_amount)
elif days <= 10 :
    fine_amount = (5 * 0.5) + ((days-5) * 1)
    print("Fine Amount : ",fine_amount)
elif days <= 30 :
    fine_amount = (5 * 0.5) + ((5) * 1) + ((days-10) * 5)
    print("Fine Amount : ",fine_amount)
else :
    print("Your membership is cancelled." )

# 8.In a company, worker efficiency is determined on the basis of the time required for a worker to complete a particular job. If the time taken by the worker is between 2 – 3 hours, then the worker is said to be highly efficient. If the time required by the worker is between 3 – 4 hours, then the worker is ordered to improve speed. If the time taken is between 4 – 5 hours, the worker is given training to improve his speed, and if the time taken by the worker is more than 5 hours, then the worker has to leave the company. If the time taken by the worker is input through the keyboard, find the efficiency of the worker.


time_taken = float(input("Enter the time taken by the worker to complete the job (in hours): "))

if time_taken >= 2 and time_taken < 3:
    print("Worker is highly efficient.")
elif time_taken >= 3 and time_taken < 4:
    print("Worker needs to improve speed.")
elif time_taken >= 4 and time_taken < 5:
    print("Worker needs training to improve speed.")
elif time_taken >= 5:
    print("Worker has to leave the company.")
else:
    print("Invalid input. Please enter a valid time.")



# 9.. Write a program to print the Armstrong numbers between 100 to 999.

armstrong_nums = []
for i in range(100, 999):
    arm = 0 
    for j in str(i):
        arm += int(j) ** 3
        if arm == i :
            armstrong_nums.append(i)
            print("The Armstrong numbers between 100 to 999 : ", armstrong_nums)


#10.Write a program to find the reverse of n digit number using While loop
    a = int(input("Enter a number : "))
    x = 0
    while a > 0:
        n = a % 10
        x = x * 10 + n
        a = a // 10
        print(x)


# 11. Write a Python program to check a list is empty or not   
     l = [1,2,3]

if len(l) == 0: print("Empty")
else : print('Not Empty')

# 12.Write a program to find the Fibonacci Series of the given number.
number = int(input("Enter a number : "))
fibonacci_series = [0, 1]
for i in range(number):
    if i <= 1:
        continue
    fibonacci_series.append(fibonacci_series[-1]+fibonacci_series[-2])
print(fibonacci_series)



# 13.Write a program to find the given number is perfect number
a = int(input("Enter a number :"))
x=1
for i in range(2,(a//2)+1):
    if a%i == 0:
        x+=i
    if x == a : print("It is a perfect number")
    else : print("It is not a perfect number")


# 14. Write a program to check whether a triangle is valid or not, when the three angles of the triangle are entered through the keyboard. A triangle is valid if the sum of all the three angles is equal to 180 degrees
a = int(input("Angle 1 : "))
b = int(input("Angle 2 : "))
c = int(input("Angle 3 : "))
if a+b+c == 180 :
    print("The triangle is valid")
else:
	print("The triangle is invalid")





# 15.A five-digit number is entered through the keyboard. Write a program to obtain the reversed number and to determine whether the original and reversed numbers are equal or not.    
n = int(input("Enter a five digit number : "))
if n>=10000 and n<=99999:
    x = 0
    a  = n
    while a > 0:
        m = a % 10
        x = x * 10 + m
        a = a // 10
        if x == n:
            print("Original and reversed numbers are equal")
        else :
            print("Original and reversed numbers are not equal")
        else:
            print("Please enter a five digit number")
