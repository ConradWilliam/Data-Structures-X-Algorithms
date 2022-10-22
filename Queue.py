from queue import Queue  # watch out with the capital letters

# Making the queue
queuename = Queue()

# We use .put() to insert value and .get() to pop the first one.
# You can think this as a normal queue

queuename.put(1)  # adds int 1 to index 0
# To access the queue, you need to change it to list
print(list(queuename.queue))
# Output : [1]

queuename.put(2)  # adds int 2 to index 1
print(list(queuename.queue))
# Output: [1,2]

queuename.get()  # removes index 0 (int 1)
print(list(queuename.queue))
# Output: [2]

# We can simulate the same effects using normal list, but the longer the queue
# the more ineffecient it becomes

queuename.append(1)
print(queuename)
# Output : [1]

queuename.append(2)
print(queuename)
# Output: [1,2]

queuename.pop(0)  # 0 is the index number
print(queuename)
# Output: [2]