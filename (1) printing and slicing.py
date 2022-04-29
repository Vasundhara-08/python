# to print a simple line
print("Goodbye, World!")

#to multiply print the same comment 
print(10*"I love Python ")

#represents blank space
print()
print("")

#different types of techniques to print 
print(12)
print(float(12.0))

#to not print the comment in new line 
print("Hi" ,end=" ")   # we use end here so that the next comment continuos from the same line
print("my" ,end=" ")
print("name is \n vasu \t1")  # same as c++ "\n" refers to new line and "\t" refers to tab(space)

# string slicing 
str="Today is a Good day"
    #01234 67 9 .... ...  <<-(these are the index)
print(str[0:3])   # here index 0 to 3 will  be printed and 3 is excluding
print(len(str))   # prints the length
print(str[:])     # if u leaves empty it print the whole comment
print(str[3:7])   # starts from index 0 prints index 3 to 6 bcz 7 is excluded
print(str[3:])    # prints from 3rd index to further.....
print(str[:7])    # prints before index 7
print(str[::2])   # given 2 after two semicolon skips one character

#negative or reverse string slicing
str="MY_COLLEGE_IS_IN_CHANDIGARH"
#    0123456789.......  <<-(these are the index)
print(str[-4:])       #prints from the end that is "GARH"
print(str[-8:-1])     #prints A to R ANDIGAR bcz -1 index is excluded
print(str[::-1])      #it reverse the string
print(str[::-2])      #first it reverse than it leaves one space 
print(str[-16:-8:-1]) #