# # def insertion_sort(list_a):
# #     indexing_length = range(1, len(list_a))
# #     for i in indexing_length:
# #         value_to_sort = list_a[i]

# #         while list_a[i-1] > value_to_sort and i > 0:
# #             list_a[i], list_a[i-1] = list_a[i-1], list_a[i]
# #             i = i - 1

# #     return list_a

# # print(insertion_sort([13,45,23,12,1,5]))

# def bubble_sort(list_a):
#     indexing_length = len(list_a)-1
#     sorted = False

#     while not sorted:
#         sorted = True
#         for i in range(0, indexing_length):
#             if list_a[i] > list_a[i+1]:
#                 sorted = False
#                 list_a[i], list_a[i+1] = list_a[i+1], list_a[i]
        
#     return list_a
# print (bubble_sort([23,255,12,77,3,67]))

# Define your Node class below:
class Node:
  def __init__(self,value,next_node = None):
    self.value =value
    self.next_node = next_node

  def get_value(self):
    return self.value
  
  def get_next_node(self): #These should return the corresponding values from self.
    return self.next_node
    
  def set_next_node(self,next_node):
    self.next_node = next_node

my_node = Node(34);
print(my_node.get_value())
  

