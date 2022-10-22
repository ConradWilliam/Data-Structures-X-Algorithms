# # MergeSort in Python

# def mergeSort(array):
#     if len(array) > 1:

#         #  r is the point where the array is divided into two subarrays
#         r = len(array)//2
#         L = array[:r]  
#         M = array[r:]

#         # Sort the two halves
#         mergeSort(L)
#         mergeSort(M)

#         i = j = k = 0
#         # Until we reach either end of either L or M, pick larger among elements L and M and place them in the correct position at A[p..r]
#         while i < len(L) and j < len(M):
#             if L[i] < M[j]:
#                 array[k] = L[i]
#                 i += 1
#             else:
#                 array[k] = M[j]
#                 j += 1
#             k += 1
#         # When we run out of elements in either L or M,
#         # pick up the remaining elements and put in A[p..r]
#         while i < len(L):
#             array[k] = L[i]
#             i += 1
#             k += 1

#         while j < len(M):
#             array[k] = M[j]
#             j += 1
#             k += 1

# # Print the array
# def printList(array):
#     for i in range(len(array)):
#         print(array[i], end=" ")
#     print()


# # Driver program
# if __name__ == '__main__':
#     array = [1,2,3,4,5,6]
#     mergeSort(array)
#     print("Sorted array is: ")
#     printList(array)

def merge_sort(arr):
    if len(arr) > 1:
        left_arr = arr[:len(arr)//2]
        right_arr = arr[len(arr)//2:]

        #recursive
        merge_sort(left_arr)
        merge_sort(right_arr)

        #merge
        i = 0   #left_arr index
        j = 0   #right_arr index
        k = 0   #merged arr index
        while i < len(left_arr)and j < len(right_arr):
            if left_arr[i] < right_arr[j]:
                arr[k] = left_arr[i]
                i += 1
            else:
                arr[k] = right_arr[j]
                j += 1
            k += 1
        while i < len(left_arr):
            arr[k] = left_arr[i]
            i += 1
            k += 1
        while j < len(right_arr):
            arr[k] = right_arr[j]
            j += 1
            k += 1
    return arr
arr = [2,5,4,32,55,67,778,4,344]             
print(merge_sort(arr))