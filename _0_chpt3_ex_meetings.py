# Meetings

# need to split the intervals into the amount of times is has
# check what is the longest meeting time
# create lists with the meeting values, if there are 2, then 2.
# compare the lists with each index slot. 
# if they overlap return false

# # Version 1
# def meetings(intervals):

#     for meet in intervals:

#         return meet
    
# print(meetings(intervals = [[0,30],[5,10],[15,20]]))
# I was too tired to do anything, could not even loop true this intervals.

# # version 2
# def meetings(intervals):
#     start_times = []
#     end_times = []
#     sorted_starts = []
#     for start, end in intervals:
#         #print(f"start: {start}")
#         #print(f"end: {end}")
#         start_times.append(start)
#         #print(f"start_times: {start_times}")
#         end_times.append(end)
#         #print(f"end_times: {end_times}")
        
#     sorted_starts = sorted(start_times)
#     print(f"Sorted_times: {sorted_starts}")
    
#     biggest_meet = max(intervals, key=lambda meet:meet[1] - meet[0])
#     print(f"biggest_meet: {biggest_meet}")
    
#     for start, end in intervals[1:]:
#         if end_times[-1] < biggest_meet[-1]:
#             return False
#         else:
#             return True

# print(meetings(intervals = [[0,30],[5,10],[15,20]]))
# print(meetings(intervals = [[7,10],[2,4]]))    
    
# Version 3
def meetings(intervals: list):
    intervals.sort() # sorts the meetings with the correct start times
    current_end_times = intervals[0][1] # take the first meeting of intervals and grab the end time
    
    for start, end in intervals[1:]: # as we grabbed the first meeting before, we only search true the remaining meetings
        if start < current_end_times: # we now compare the next start time with the previous end time: Overlap-check
            return False
        current_end_times = end # update the end times with the next iteration
    
    # For anything else, it will be possible to have more meetings during the day. 
    # Meaning TRUE is what we return
    return True

    
print(meetings(intervals = [[0,30],[5,10],[15,20]]))
print(meetings(intervals = [[7,10],[2,4]]))