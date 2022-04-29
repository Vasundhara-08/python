fruits=["mango","apple","grapes","banana","plum","78"]  #[] indicates tuple 
fruit=("mango","apple","grapes","banana","plum","78")   #() does not print any items
fruits_1=[["mango",1],["apple",6],["grapes",9],["banana",5],["plum",7]]  #[[]] list in list
print(fruit)

# for printing items in list we use
print(fruits[0],fruits[1])

# but if there are a lot of items then we use 
# for loop to automatically print all the items
for item in fruits:
    print(item)

for item in fruits:
    print(item)    

#print list in list for loop
for item,number in fruits_1:
    print(item,number)
    print("The item is" , item,"and the total no. =" ,number )   #known as iteration

#printing items using dict function 
dict1=dict(fruits_1)       #dict1 is the dictionary were to store items
print(dict1)               # prints >> {'mango': 1, 'apple': 6, 'grapes': 9, 'banana': 5, 'plum': 7}

#for loop using dictionary items
for item in dict1:
    print(item)

for item in dict1:
    print(dict1)    
