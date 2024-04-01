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

=======
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

>>>>>>> 80ad7b23b145cde6ee7b497c72f48d960e2617a4
                