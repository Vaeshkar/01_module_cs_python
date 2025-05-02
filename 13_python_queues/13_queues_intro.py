class Queue:
    def __init__(self):
        self.queue = []
        
    def enqueue(self, element):
        """
        Insert an element at the read of the queue.
        """
        self.queue.append(element)
        
    def dequeue(self):
        """
        Remove and return the element at the from fo the queue.
        """
        if self.isEmpty():
            return None
        return self.queue.pop(0)
    
    def peek(self):
        """
        Return the front eement without removing it.
        """
        if self.isEmpty():
            return None
        return self.queue[0] # Return the index position 0
    
    def isEmpty(self):
        """
        Check if the queue is empty.
        """
        return len(self.queue) == 0
    
    def size(self):
        """
        Return the number of elements in the queue.
        """
        return len(self.queue)
    
# Example usage
myQueue = Queue() # assign a variable to the Class

# Adding 3 new items in the Queue() with enqueue Method
myQueue.enqueue('A')
myQueue.enqueue('B') 
myQueue.enqueue('C')

# Print Tests
print("Queue:", myQueue.queue) # Output: ['A', 'B', 'C'] Queue_List is called

print("Dequeue:", myQueue.dequeue()) # Output: Removes: 'A'

print("Peek:", myQueue.peek()) # Output: Front element is returned 'B' 

print("isEmpty:", myQueue.isEmpty()) # Output: False

print("Size:", myQueue.size()) # Output: While 'A' is removed the size will be 2
