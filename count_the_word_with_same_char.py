def main():
    list=['abc','good','god','abc','good','bca','God','ccc','ogd','ddd','ccc']
    removeDuplicates(list)

def removeDuplicates(list):
    sortedList=[]
    for i in range(0,len(list)):
        str=list[i]
        word=""
        for j in str.lower():
            if j not in word:
                word=word+j
        sort="".join(sorted(word))
        sortedList.append(sort)
    print(sortedList)
    compare(sortedList)

def compare(sortedList):
    words=[]
    for i in range(0,len(sortedList)):
        for j in range(i+1,len(sortedList)):
            if sortedList[i]==sortedList[j]:
                if sortedList[j] not in words:
                    words.append(sortedList[j])

    print("count :",len(words))


main()