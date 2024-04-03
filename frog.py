# There are frogs walking in a line represented in the form of a list. The numbers in the list are the size of frogs. A frog(at position i) will eat the previous frog (i-1), if the previous frog is smaller in size. Print the alive frogs in the list 

# Input : [1,2,5,4,3,2,2]
# Output : [5,4,3,2,2]
# Explanation : Frog (1) ate Frog(0); Frog(2) ate Frog (1). Rest of the frogs are alive
# Input : [4,3,3,2,1]
# Output : [4,3,3,2,1]


def frog(i):
    while i<len(list):
        if list[i-1]<list[i]:
            list.pop(i-1)
        i+=1
    print(list)

list=[1,4,1,3,1,2,2,1]
i=1
frog(i)

