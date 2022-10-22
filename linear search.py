def worstcase(z,value):
    z = []
    for i in range(len(arr)):
        if arr[i] == value:
            z.append(i)
    return z
   
arr = [11,423,172,30,910,9,2,45,172]
value = 172
print(worstcase(arr,value))