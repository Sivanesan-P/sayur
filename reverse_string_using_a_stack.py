# Reverse a string: Given a string, reverse it using a stack.
# Eg : Hello -> olleH

str=input("Enter the string: ")
stack=[char for char in str]
for i in range(len(stack)):
    pop=stack.pop()
    print(pop,end="")
