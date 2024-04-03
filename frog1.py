def frog(i):
    for i in range(i,len(list)):
        j=1
        while j<len(list):
            if list[j-1]<list[j]:
                list.pop(j-1)
            j+=1
    print(list)

list=[1,1,1,5,1,4,3,2]
i=1
frog(i)