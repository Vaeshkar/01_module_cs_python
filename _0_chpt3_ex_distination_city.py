# Destination City

### GOAL ###
# find the city that never is at the starting position
# is is the destination

### TASK / Breakdown ###
# Array of paths
# parameters: cityA and cityB
# paths[i] = [cityA, cityB]

# Extract all citiesA into a set() <- O(1) quick search
# Check all end_citiesB and return the one that is not in citiesA set()

### Complexity Calculation ###
# 1st for loop: O(n) + 
# 2nd for loop: O(n) * 
# 3rd  if condi O(1) =
# Complexity of O(n)

### Grab the cities and build two variables to compare them


### How to compare ###
# Loop true citiesB
## check if cityB != in citiesA
## return city not in citiesA

####
### ["London","New York"]
###          ["New York","Lima"]
###                     ["Lima","Sao Paulo"]
###     ["B","C"]
### ["D","B"]
###         ["C","A"]
####

##########################

def destination_city(paths:list):
    '''
    ### GOAL
    Find the city that never is at the starting position is is the destination
    
    Args:
        paths: list of values
        
    Returns:
        A f-string message with the destination city
    '''
    # create two lists of cities
    citiesA = []
    citiesB = []
    
    # loop true the paths and add them to the two variables
    for cityA, cityB in paths:
        citiesA.append(cityA)
        citiesB.append(cityB)

    # convert the citiesA to a set <- O(1) quick search
    citiesA_set = set(citiesA)
    #check if the set convertion is done:
    #print(f"\ncitiesA as a set: {citiesA_set}")
    
    # check if cityB is NOT in citiesA_set.
    for city in citiesB:
        if city not in citiesA_set:
            return f"This is our Destitation City: {city}."
    
    #return a mini else
    return "No destination given."

print(destination_city([["London","New York"], ["New York","Lima"], ["Lima","Sao Paulo"]]))
print(destination_city([["B","C"], ["D","B"], ["C","A"]]))
print(destination_city([["",""]]))

##########################
