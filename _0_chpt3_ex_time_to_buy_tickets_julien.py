from collections import deque 

#############
# Psuedo code

# Function timeRequiredToBuy(tickets, k):
#     Initialize queue as a list of (index, tickets_needed) for each person
#     Initialize time = 0  // To count the total time elapsed
#     While queue is not empty:
#         Remove the first person (index, remaining_tickets) from the queue
#         Increment time by 1  // Each person buys one ticket per second
#         If remaining_tickets > 1:
#             Add (index, remaining_tickets - 1) to the end of the queue
#         If index == k AND remaining_tickets == 1:
#             Return time  // Stop when person k finishes buying all their tickets

def timeRequiredToBuy(tickets, k):
    queue = deque(enumerate(tickets))  # Create a queue of (index, tickets_needed)
    time = 0
    while queue:
        index, remaining_tickets = queue.popleft()  # Get the person at the front
        time += 1  # Buying one ticket takes 1 second
        if remaining_tickets > 1:
            queue.append((index, remaining_tickets - 1))  # Move person to end if they need more tickets
        if index == k and remaining_tickets == 1:
            return time  # Stop when person k finishes buying
# Example cases
print(timeRequiredToBuy([2, 3, 2], 2))  # Output: 6
print(timeRequiredToBuy([5, 1, 1, 1], 0))  # Output: 8