#For the linked list, the first step is to create a class representing it. For now, we just want a head attribute when creating an empty list.
class Node:
  def __init__(self,value,next_node = None): #Basically, it has a value and the reference to the next node. We add a default value (None) to the next parameter to make it more flexible to use when creating new nodes.
    self.value =value
    self.next_node = next_node

  def get_value(self): #get the value or data of node
    return self.value
  
  def get_next_node(self): #These should return the corresponding values from self.
    return self.next_node

  def set_next_node(self,next_node):#set the data to the required node
    self.next_node = next_node

# Instantiate the new node.
# We can access the value and the next_node attributes.
# But with the flexibility of the next parameter, we can also use it by passing the next node reference.
my_node = Node(1)
my_node.value
my_node.next_node
print(my_node.get_value())

next_node = Node(2)
my_node = Node(1, next_node)
my_node.value #1
print (my_node.next_node.value)

class LinkedList: #the first step is to create a class representing it. For now, we just want a head attribute when creating an empty list.
    def __init__(self):
        self.head = None

        linked_list = LinkedList()
    def append(self, value):
        if self.is_empty():
            self.head = Node(value)
            return

        current_node = self.head

        while current_node.next is not None:
            current_node = current_node.next

        current_node.next = Node(value)

    def prepend(self, value):
        self.head = Node(value, self.head)

    def remove(self, value):
        if self.is_empty():
            return

        if self.head.value == value:
            self.head = self.head.next
            return

        current_node = self.head

        while current_node.next is not None:
            if current_node.next.value == value:
                current_node.next = current_node.next.next
                return

            current_node = current_node.next

    def search(self, value):
        found = False
        current_node = self.head

        while not found and current_node is not None:
            found = current_node.value == value
            current_node = current_node.next

        return found

    def is_empty(self):
        return self.head is None

    def size(self):
        list_length = 0
        current_node = self.head

        while current_node is not None:
            list_length += 1
            current_node = current_node.next

        return list_length

    def print_all(linked_list):
        print('All values:', end=' ')
        current_node = linked_list.head

        while current_node is not None:
            print(current_node.value, end=' ')
            current_node = current_node.next

        print()

    def print_found(linked_list, value):
        found = linked_list.search(value)
        print('For value:', value, '-->', 'Found:', found, )

    def print_size(linked_list):
        list_length = linked_list.size()
        print('Size:', list_length)

        linked_list.append(3)
        print(linked_list)  # 1
        print(linked_list)  # 1