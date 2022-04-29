from black import mypyc_attr


my_fun="this is about some commonly used functions in python"
print(my_fun.isalpha())           #neither alphabet nor numeric bcz it contain spaces btw
print(my_fun.endswith("python"))  #true statement
print(my_fun.count("o"))          #6
print(my_fun.capitalize())        #it only capitalize first letter
print(my_fun.find("on"))          #it gives address where the findv str is present
print(my_fun.upper())             #capitalize all the letters
print(my_fun.replace("this","that"))
print(len(my_fun))

# LIST FUNCTIONS

fruits=["mango","apple","grapes","banana","plum","78"]
print(fruits)
print(fruits[5])

number=[56,9,43,1]
number.sort()        #first we need to apply the function
number.reverse()     #reverse the string
print(number)        #then we print to run the function
print(max(number))   #prints the highest value number
print(min(number))   #prints the lowest value number
number.append(90)    #to add something at the end 
number.insert(3,0)   #insert the number at particular index 
number.remove(1)     #removes the number
number.pop()         #removes the last element 
number[2]=100        #it works same as insert function
print(number)

