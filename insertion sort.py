# z = [5,2,4,6,1,3]
# x = 1
# print("Array z before sorting.")
# print(z)
# print("size of array Z = ")
# print(len(z))


# while x < len(z):
#     c = z[x]
#     y = x-1
#     while y >= 0 and z[y] >  c:
#         z[y+1] = z[y]
#         y=y-1
#     z[y+1] = c
#     print("Round: ")
#     x=x+1
# print("Array after sorting")
# print(z)

# define a list
num=[20,35,45,10,60]
print('List before Insertion Sort')
for n in num:
    print(n,end=' ')
# run an outer loop i from 1 to len(num) to repeat the process of insertion sort
for i in range(1,len(num)):
    # x to be inserted at proper place
    x=num[i]
    # run an inner while loop j for insertion sort from i-1 to 0
    j=i-1
    while j>=0:
        # now check if the value of x is greater than num[j] then shift the number num[j] towards right else break the inner loop j
        if x>num[j]:
            num[j+1]=num[j]
        else:
            break
        j=j-1
    # outside the body of inner loop j insert the value of x at num[j+1] position
    num[j+1]=x
# print the sorted list
print('\n\nList after Insertion Sort')
for n in num:
    print(n,end=' ')





