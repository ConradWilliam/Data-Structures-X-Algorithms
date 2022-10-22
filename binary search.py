def sort(ListA):
    for i in range(len(ListA)-1,0,-1):
        for j in range(i):
            if ListA[j]>ListA[j+1]:
                temp = ListA[j]
                ListA[j]=ListA[j+1]
                ListA[j+1]=temp

ListA = [31, 41,59, 26, 41,58]
sort(ListA)

print(ListA)