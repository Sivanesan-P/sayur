def parentheses_checker(input):
    for i in input:
        if i==')' and not list:
            print("parentheses is missing")
            return
        elif i=='(':
            list.append(i)
        elif i==")" and len(list)>=1:
            list.remove('(')
    if not list:
        print("parentheses are balanced")  
    else:
        print("parentheses is missing")


input=input("enter:")
list=[]
parentheses_checker(input)

def parentheses_checker(input):
    for i in input:
        if i==')' and not list:
            print("parentheses is missing")
            return
        elif i=='(':
            list.append(i)
        elif i==")" and len(list)>=1:
            list.remove('(')
    if not list:
        print("parentheses are balanced")  
    else:
        print("parentheses is missing")


input=input("enter:")
list=[]
parentheses_checker(input)

                