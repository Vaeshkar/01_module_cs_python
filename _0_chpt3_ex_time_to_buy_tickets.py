#######################
# Time to Buy Tickets #
#######################

# Pseudocode:
# Initialize a queue with (index, tickets_needed) for each person.
# Start a loop:
# Remove the first person from the queue.
# Reduce their ticket count.
# If they still need tickets, reinsert them at the end.
# If not, check if this was person k:
# If yes, return the elapsed time.
# Otherwise, keep going.

def time_to_buy_tickets(tickets: list, k: int):
    queue = list(enumerate(tickets)) # list with: index and tickets
    time_spend = 0
    front = 0
    
    # queue = [(0,2), (1, 3), (2,2)]
    # index = 0
    # ticket_left = 2
    
    while queue:
        index, tickets_left = queue[front]
        tickets_left -= 1 # remove 1 ticket
        time_spend += 1 # increase time
        queue[front] = (index, tickets_left) # update the ticket count
    
        if tickets_left == 0: # check if the tickets are done
            if index == k: # also check if it is our target person
                return time_spend # if so stop and return the time_spend
            queue.pop(front) # remove that person from the queue
        else:
            queue.append(queue.pop(front)) # move that person to the back

print(time_to_buy_tickets([2,3,2],2)) # 6
print(time_to_buy_tickets([5,1,1,1],0)) # 8


### changes made ###
def time_to_buy_tickets(tickets: list, k: int):
    queue = list(enumerate(tickets)) # list with: index and tickets
    time_spend = 0
    print(type(queue[0]))
    while queue:
        index, tickets_left = queue.pop(0)
        tickets_left -= 1 # remove 1 ticket
        time_spend += 1 # increase time
    
        if tickets_left == 0: # check if the tickets are done
            if index == k: # also check if it is our target person
                return time_spend # if so stop and return the time_spend

        else:
            queue.append((index, tickets_left)) # move that person to the back

print(time_to_buy_tickets([2,3,2],2)) # 6
print(time_to_buy_tickets([5,1,1,1],0)) # 8