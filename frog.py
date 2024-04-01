# There are frogs walking in a line represented in the form of a list. The numbers in the list are the size of frogs. A frog(at position i) will eat the previous frog (i-1), if the previous frog is smaller in size. Print the alive frogs in the list 

# Input : [1,2,5,4,3,2,2]
# Output : [5,4,3,2,2]
# Explanation : Frog (1) ate Frog(0); Frog(2) ate Frog (1). Rest of the frogs are alive
# Input : [4,3,3,2,1]
# Output : [4,3,3,2,1]


list=[1,4,1,3,1,2,2,1]
m=list[0]
list1=[]
for i in range (len(list)):
    for j in range(1,2):
        if len(list)!=1:
            if m<list[j]:
                list.remove(m)
                m=list[0]
            else:
                list1.append(m)
                list.remove(m)
                m=list[0]
        else:
            list1.append(m)

print(list1)
