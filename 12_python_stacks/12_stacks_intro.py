class Stack:
    def __init__(self):
        self.items = [] # emtpy list
        
    def push(self, item): #
        """
        Add an element to the top of the stack.
        """
        self.items.append(item) # add the a new element on the top of the stack with append()
        
    def pop(self):
        """
        Remove and return the top element of the stack. 
        """
        if self.is_empty(): # check instance method: is_empty below
            return None # or raise an exception
        return self.items.pop() # remove and return the top element of the stack
    
    def peek(self):
        """
        Return the top element without removing it.
        """
        if self.is_empty():
            return None 
        return self.items[-1] # return the last index element of the stack for a peek. Reminder () is not a list!!
    
    def is_empty(self):
        """
        Check if the stack is empty.
        """
        return len(self.items) == 0 # check is the number of len() is equal to Zero. Meaning empty == True
    
    def size(self):
        """
        Return the number of elements in the stack.
        """
        return len(self.items) # as the doctring here above describes
    
# example usage:
stack = Stack()
stack.push(10)
stack.push(20)
print("Top element:", stack.peek()) # Output: top element: 20
print("Pop element:", stack.pop()) # Output: element: 10
print("Is empty?", stack.is_empty()) # Output: Is empty? False
print("Stack size:", stack.size()) # Stack size after removing e20, will be 1(One)
