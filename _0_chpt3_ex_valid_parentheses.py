#####################
# Valid Parentheses #
#####################

# Pseudo code
""" 
string s with only these chars: (), {}, []
Check is the brackets are valid, by the following criteria:
- Open and closing bracket
- Closed in the correct order
- Every closing bracket matches the opening bracket

Input: String of bracket "(), [], {}"
Output: Boolean

## Steps ##
Create a stack (list in Python).
Use a dictionary for bracket pairs: {'(': ')', '{': '}', '[': ']'}.
Iterate over s:
If an opening bracket, push it to the stack.
If a closing bracket, check if it matches the top of the stack.
Return True if stack is empty at the end, False otherwise.
"""

def valid_parentheses(s:str):
    '''
    ### GOAL ###
    string s with only these chars: (), {}, []
    
    Args:
        s:str with char
        
    Returns:
        Bool True or False
    '''
    stack = []
    pairs = {'(':')','[':']','{':'}'}

    # iterate over the s(str)
    for bracket in s:
        # print(f"bracket: {bracket}") # view the bracket
        if bracket in pairs.keys(): # check the LEFT SIDE with keys()
            stack.append(bracket) # move the bracket to the stack
        elif bracket in pairs.values(): # check the RIGHT SIDE with values()
            if not stack or pairs[stack.pop()] != bracket: 
            # hard logic: if the right bracket is NOT in the stack or in the pairs after pop()
            # With pop() we keep the bracket we need from our pairs dict to compare
            # We find a True in out if statement
                return False # return false
    return not stack # All bracket matched. 

print(valid_parentheses("()")) # True
print(valid_parentheses(")(")) # False
print(valid_parentheses("()[]{}")) # True
print(valid_parentheses("(]")) # False
print(valid_parentheses("([])")) # True

