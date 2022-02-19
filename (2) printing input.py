# to add two numbers
num1 = 1
num2 = 2
sum = num1+num2 
print("the sum of {0} and {1} is {2}" .format(num1 ,num2 ,sum) )

# to add two numbers provided by user input
num1 = input(" The first num is: ")
num2 = input(" The second num is: ")
multiplication = int(num1) * int(num2)
print("The multiplication of {0} and {1} is {2}" .format(num1 ,num2 ,multiplication))

# to print the input value {in a short way!}
a = int(input())
b = int(input())
print(a+b)
print(a-b)
print(a*b)

# to change the value during the user input (concatenate)

print("Enter the number u want to print:")
#var here is in string form
var1 =input()                                     
print("the number u entered was : " ,var1)
# if we directly put var+10 it gives error bcz we need to convert str in int 
print("the number it modified in here is",int(var1)+10)


