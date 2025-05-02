###class###
class Queue:
    def __init__(self):
        self.queue = []

    def enqueue(self, element):
        """Insert an element at the rear of the queue."""
        self.queue.append(element)

    def dequeue(self):
        """Remove and return the element at the front of the queue."""
        if self.is_empty():
            return "Queue is empty"
        return self.queue.pop(0)

    def peek(self):
        """Return the front element without removing it."""
        if self.is_empty():
            return "Queue is empty"
        return self.queue[0]

    def is_empty(self):
        """Check if the queue is empty."""
        return len(self.queue) == 0

    def size(self):
        """Return the number of elements in the queue."""
        return len(self.queue)
    
###method###
def ticket_time(tickets, target):
    queue = Queue()
    seconds = 0
    for index in range(len(tickets)):
        if index == target:
            buyer = [tickets[index], True]
        else:
            buyer = [tickets[index], False]
        queue.enqueue(buyer)
    while not queue.is_empty():
        actual_buyer = queue.dequeue().copy()
        actual_buyer[0] -= 1
        seconds += 1
        if actual_buyer[0] == 0:
            if actual_buyer[1] == True:
                return seconds
            continue
        else:
            queue.enqueue(actual_buyer)
    return seconds

###testing###
input_1 = [2, 3, 2]
target_1 = 2
output_1 = 6

input_2 = [5, 1, 1, 1]
target_2 = 0
output_2 = 8

input_3 = [1, 1, 1, 1]
target_3 = 2
output_3 = 3

input_4 = [4, 5, 2, 6]
target_4 = 1
output_4 = 12

input_5 = [10, 9, 8, 7]
target_5 = 2
output_5 = 31

def test():
    for n in range(1, 6):
        input = globals()[f"input_{n}"]  # Fetch the actual variable
        target = globals()[f"target_{n}"]  # Fetch the actual variable
        output = globals()[f"output_{n}"]  # Fetch the actual variable
        print(f"input_{n}, target_{n}, output should be {output} and it is: {ticket_time(input, target)}")

test()