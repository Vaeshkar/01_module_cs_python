
# String ends with?
def solution(text, ending):
    # new variable called slice
    # we take the len() of 'ending', we nr. 2
    # slice_len = 2
    
    # we want to slide 'text' and keep 'ending'
    # start slicing from the back: -1
    # with slicing it would look like this [-1:]
    # Integrate/use 'slice_len' with 'text': text[-slice_len:]
    
    # "samurai"
    # "0123456"
    #      "ai"
    #      "01"
    #slice_len = -2
    #slice_len "-2"
    
    # "fails","ails"
    #   text , ending
    # slice_len = len(ending) = 4
    # text[-ending:]
    # "ails" = text
    # "01234"
    #    "-4"
    
    # text = "ails"
    # ending = "ails"
    slice_len = len(ending) # = an Integer now!
    
    if slice_len == 0:
        return True

    if text[-slice_len:] == ending:
        return True
    else:
        return False

print(f"samurai, ra: {solution('samurai', 'ra')}") # False
print(f"samurai, ai: {solution('samurai', 'ai')}") # True
print(f"sumo, omo: {solution('sumo', 'omo')}") # True
print(f"fails, ails: {solution('fails', 'ails')}") # True
print(f"abc, d: {solution('abc', 'd')}") # False
print(f"abc, '': {solution('abc', '')}") # True
