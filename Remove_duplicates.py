str=input("Enter the string : ")
list=str.split(" ")
for i in range(0,len(list)):
    str1=list[i]
    output=""
    for j in str1.lower():
        if j not in output:
            output=output+j
    print(output,end=" ")

print("\n")

for i in range(0,len(list)):
    str1=list[i]
    output=""
    for j in str1:
        if j not in output:
            output=output+j
    print(output,end=" ")


    