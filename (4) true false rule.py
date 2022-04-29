#implementing true = 1,false = 0

print(True==0)
print(False==0)
print(True==1)
print(False==1)

#logical expressions

print(True + True - True)   # (1+1-1) = 1
print(True + False + False) # (1+0+0) = 1
print(2==0)
print(None==0)
print(None==())

# and operation

print(True and False)   # 1 * 0 = 0 (returns false)
print(True and True)    # 1 * 1 = 1 (returns true)
print(False and False)  # 0 * 0 = 0 (returns false)
print(False and True)   # 0 * 1 = 0 (returns false)

# or operation

print(True or False)   # 1 + 0 = 1 (returns true)
print(True or True)    # 1 + 1 = 1 (returns true)
print(False or False)  # 0 + 0 = 0 (returns false)
print(False or True)   # 0 + 1 = 1 (returns true)

# not operation 

print(not True)      # (returns false)
print(not False)     # (returns true)

#in operation: This keyword is used to check if a container contains a value.

if 'd' in "don't copy my code":
    print("d is a part of don't copy my code")
else:
    print("d is not a part of don't copy my code")

#is operation: This keyword is used to test object identity, i.e to check if both the objects take the same memory location or not. 

