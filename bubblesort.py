# def bubble_sort(list_a):
#     indexing_length = len(list_a)-1 
#     sorted = False

#     while not sorted:
#         sorted = True

#         for i in range(0, indexing_length):
#             if list_a[i] >list_a[i+1]:
#                 sorted = False
#                 list_a[i], list_a[i+1]=list_a[i+1],list_a[i]
#     return list_a

# list_a = [2,5,6,7,3,9]
# print(bubble_sort(list_a))




def bubble(list_a):
    indexing_length = (len(list_a)-1)
    sorted = False

    while not sorted:
        sorted = True

        for i in range(0, indexing_length):
            if list_a[i] < list_a[i +1]:
                sorted =  False
                list_a[i], list_a[i+1]=list_a[i+1], list_a[i]
    return list_a

list_a = [1,6,33,7,8,99,4,90,2,55]
print(bubble(list_a))

























