# Given string str, we need to print the reverse of individual words. (dont use built in functions)
# Input : Hello World
# Output : olleH dlroW


def Split(str):
    stack=[char for char in str]
    for i in range(len(stack)):
        if stack[i]!=" ":
            list.append(stack[i])
        if stack[i]==" " or i+1==len(stack):
            for j in range(len(list)):
                pop=list.pop()
                print(pop,end="")
            print(" ",end="")




str=input("Enter the string: ")
list=[]
Split(str)





