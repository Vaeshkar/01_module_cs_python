
# String ends with?
def solution(text, ending):
    # new variable called slice
    # we take the len() of 'ending', we nr. 2
    # slice = 2
    
    # we want to slide 'text' and keep 'ending'
    # start slicing from the back: -1
    # with slicing it would look like this [-1:]
    # Integrate/use 'slice' with 'text': text[-slice:]
    
    # "samurai"
    # "0123456"
    #      "ai"
    #      "01"
    #slice = -2
    #slice "-2"
    
    # "fails","ails"
    #   text , ending
    # slice = len(ending) = 4
    # text[-ending:]
    # "ails" = text
    # "01234"
    #    "-4"
    
    # text = "ails"
    # ending = "ails"
    slice = len(ending) # = an Integer now!
    
    if ending in text[-ending:]:
        return True
    else:
        return False

print(solution("samurai", "ra"))
#print(solution("sumo", "omo"))
#print(solution("fails","ails"))