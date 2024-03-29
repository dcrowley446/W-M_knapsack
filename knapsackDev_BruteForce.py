'''
"""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""
README: W&M Knapsack Packing Algorithm Assignment - Brute Force Approach
"""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""

Created on Thu Mar 28 08:06:39 2024
@author: Dave


Problem Statement
    Pack a knapsack of limited capacity with items whose combination gives the highest value
    Each item has a different value and volume
    Goal is to use a heuristic algorithm to find the most efficient and optimal solution
    There are 10 knapsack problems total
    

My Solution
    In this file, I approached this solution through brute force. I determined every single
    combination of items, calculated their volume and value, and then kept the valid combination
    with highest value. Though slow, I believe this should give the correct answer. However,
    the output shows that I didn't find the optimal solution (highest value). I'm unsure why!


General Program Note
    This problem was an assignment during my Master of Science, Business Analytics
    degree at William & Mary. I submitted an initial solution during my coursework,
    but I re-wrote this algorithm here to re-learn the assignment and attempt to
    determine a better solution. Feedback from my initial attempt was that my
    solution was on the slower side relative to my other classmates, yet it did achieve
    the optimal solution for most problems. For my re-written solution, my result
    is pretty much the same, but I feel that I understand the code better. I will
    continue to iterate on this program to find a more optimal and efficient solution.


Code Notes
    All comments in this file are my own
    
    Section: IMPORT PACKAGES
    I added itertools for my heuristic algorithm, but time and json were there already
    
    Section: FUNCTIONS TO VALIDATE KNAPSACK PACKING ALGORITHM
    Code was largely untouched by me because the main purpose of these functions
    was for the instructor to evaluate and validate the packing solution. However,
    all comments were written by me as a way to understand and explain the code.

    Section: KNAPSACK PACKING HEURISTIC ALGORITHM - BRUTE FORCE APPROACH
    The code in this section is 100% my own. This section the only section which
    the instructor assigned us to write.
    
    Section: EVALUATION
    Code was largely untouched by me because this is where the instructor ran
    the evaluation functions to validate my solution. However, I did edit the
    output to be a bit more organized and show my solution as a percentage of
    the optimal solution.    

'''



"""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""
IMPORT PACKAGES
"""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""

import time
# used to track time of algorithm for measuring efficiency

import json
# for importing JSON file containing knapsack problems

import itertools
# used to create combinations of IDs in absolute brute force logic



"""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""
FUNCTIONS TO VALIDATE KNAPSACK PACKING ALGORITHM
"""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""

''' check contents of the knapsack to see if their total volume is greater than capacity '''
def checkCapacity(contents,knapsack_cap):
    # contents = {item_id: (volume, value), ...}
    # knapsack_cap = maximum capacity of knapsack, extracted from knapsack problem
    # return:
        # True if volume <= cap
        # False if volume > cap
        # error statement if "contents" is not a dictionary

    # initialize variable to measure the total volume of items
    volume = 0

    # if statement to confirm input is a dictionary (see else statement at bottom for alt result)
    # explanation: "isinstance() returns True if the object ("contents") is the specified type ("dict")
    if isinstance(contents,dict):
        # loop through each item that was placed in the knapsack
        # item = keys of dict = 2-element tuple of (volume, value)
        for item in contents.keys():
            # extract volume from each item and add to total volume
            volume += contents[item][0]
        # return True if at/under capacity, or return False if over capacity
        if volume <= knapsack_cap:
            return True
        else:
            return False
    # if input of knapsack contents is not a dictionary, returns an error statement
    else:
        print('function checkCapacity() requires a dictionary')


''' calculate the total value of all items placed in the knapsack '''
def knapsack_value(contents):
    # contents = {item_id: (volume, value), ...}
    # return:
        # total value of items
        # error statement if "contents" is not a dictionary
    
    # initialize variable to measure the total value of items
    value = 0.0
    
    # if statement to confirm input is a dictionary (see else statement at bottom for alt result)
    if isinstance(items,dict):
        # loop through each item that was placed in the knapsack
        # item = keys of dict = 2-element tuple of (volume, value)
        for item in contents.keys():
            # extract value from each item and add to total value
            value += contents[item][1]
        return(value)
    else:
        print('function knapsack_value() requires a dictionary')


''' extract knapsack problems from JSON file and converts list of knapsack items to key:value pairs '''
# conversion: [[volume1,value1], [volume2,value2], ...] --> {0:(volume1,value1), 1:(volume2,value2), ...}
# now I can extract each item of the knapsack based on sequential keys

def getData():
    # input = none
    # return:
        # x = list of dictionaries, where each dictionary is a knapsack problem
        # witihn x, the initial list of lists of items is converted to a dictionary of items
        # in the format of {item #1: (volume of item #1, value of item #2), ...}
        # item # = sequential integer starting at 0
    
    # JSON file contains 10 knapsack problems (each in the form of a list of dictionaries
    # problem format = {"cap" : float, "opt" : float, "source" : string, "data" : list of 2-element lists}
    # further details about these three key/value pairs:
        # "cap" : float number representing the capacity of the knapsack
        # "opt" : float number for optimal value of full knapsack
        # "source" : string with information indiciating the source of the knapsack problem (irrelevant to analysis)
        # "data" : list of lists containing each item in the format of [[volume1, value1], [volume2, value2], ...]
    
    # open, load, close JSON file
    f = open('knapsack.json','r')
    x = json.load(f)
    f.close()
    
    # loop through each knapsack problem
    for i in range(len(x)):
        
        # extract the knapsack problem items into myData through indexing (use 'data' key to extract associated value)
        myData = x[i]['data']
        
        # initialize current knapsack and convert from list of lists to an empty dictionary
        x[i]['data'] = {}
        
        # fill empty dictionary with list of items
        # format is now: {0:(volume1, value1), 1:(volume2, value2), ...}
        for j in range(len(myData)):
            x[i]['data'][j] = tuple(myData[j])
            
            # to explain how this happens:
                # x[i]['data'][j] --> indexing to get to the value of the given key:value pair
                # and then assign that value as a tuple of the item's volume & value
                # in the above indexing, "j" is the key and (volume,value) is the value in the key:value pair
                # in other words, I'm telling python that for the key of "j", assign the value of (volume,value)
                # this works because of dictionary indexing: dictionary[key] = value
                # indexing the dictionary using the key will provide the key's associated value

    return x



"""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""
KNAPSACK PACKING HEURISTIC ALGORITHM - BRUTE FORCE APPROACH
"""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""
# this portion of code is written by me (as was the main assignment for this project)

''' heuristic knapsack packing algorithm '''
def loadKnapsack(items, knapsack_cap):
    # items = dictionary of items from a knapsack problem
    # knapsack_cap = maximum capacity of knapsack, extracted from knapsack problem
    # return:
        # items_to_pack = list of item IDs (keys of knapsack dictionary) for items to be packed
    

    # CODE #1 PLAN
    # 1. produce every single combination of items --> "ID_combinations"
    # 2. calculate the volume and value for each combination
    # 3. determine if the volume is at/under or over knapsack capacity
    # 4. store the combination with the highest value and valid capacity
    # 5. output that combination as items_to_pack
    

    # CODE #1 EXECUTION
    
    # create list of the item IDs
    item_IDs = [i for i in items.keys()]
    
    # generate a list of lists for every possible combination of item IDs
    ID_combinations = list(itertools.chain(*[itertools.combinations(item_IDs, i) for i in range(1, len(item_IDs) + 1)]))
    ID_combinations = [list(comb) for comb in ID_combinations]
    # explanation: create list of tuples, then convert to lists...required intermediary step because of how itertools works
    # example output:
        # item_IDs = [0,1,2]
        # ID_combinations = [[0],[1],[2],[0,1],[0,2],[1,2]]
        # no replacemenets (meaning, no repeated number combinations like [2,2])
    
    # initialize variable to store highest value of looped through combinations so far
    highest_value = 0
    
    # initialize list of item IDs for packed items
    items_to_pack = []
    
    # loop through each combination ("comb") in list ID_combinations
    for comb in ID_combinations:
        # initialize variables to sum the volume and value of each combination
        comb_volume = 0
        comb_value = 0
        # loop through each ID in the current combination
        for ID in comb:
            # store the sum of total volume and value for combination in respective variables
            comb_volume += items[ID][0]
            comb_value += items[ID][1]
        # conditional to determine if summed volume meets capacity requirement of knapsack
        if comb_volume <= knapsack_cap:
            # True = volume is at or under capacity (solution is valid)
            comb_capacity = True
        else:
            # False = volume is over capacity (solution is not valid)
            comb_capacity = False
        
        # conditional to determine if the valid solution has the highest value
        if (comb_capacity == True) and (comb_value > highest_value):
            items_to_pack = comb
   
    return items_to_pack
        


"""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""
EVALUATION
"""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""

''' get data and define problem IDs '''
# store knapsack problems in probData
probData = getData()

# count number of knapsack problems
problems = range(len(probData))

# turn off (True) or turn on (false) error messages during evaluation
silent_mode = False


''' write outputs for error messages '''
# written by W&M instructor

error_bad_list_key = ''' 
A list was received from load_knapsack() for the item numbers to be loaded into the knapsack.  
However, that list contained an element that was not a key in the dictionary of the items that were 
not yet loaded. This could be either because the element was non-numeric, it was a key that was 
already loaded into the knapsack, or it was a numeric value that didn't match with any of the 
dictionary keys. Please check the list that your load_knapsack function is returning. It will be 
assumed that the knapsack is fully loaded with any items that may have already been loaded and 
a score computed accordingly. 
'''

error_response_not_list = '''
load_knapsack() returned a response for items to be packed that was not a list. 
Scoring will be terminated
'''


''' loop through and solve each knapsack problem '''
# "problems" = # of knapsack problems = number of dictionaries listed in JSON file
for problem_id in problems:
    
    # initialize dictionary to store items placed in knapsack
    in_knapsack = {}
    
    # extract capacity of knapsack 
    # (slice the knapsack problem dictionary using key 'cap' which provides the value of capacity)
    knapsack_cap = probData[problem_id]['cap']
    
    # extract dictionary of items and store in "items" variable
    # format: {0,(volume1,value1), 1,(volume2,value2), ...}
    items = probData[problem_id]['data']
    
    # initialize errors to be False to start evaluation
    # (if there are errors, this will then be set to True and code will output error message)
    errors = False
    
    # initialize items_to_pack for it to be used in loadKnapsack
    items_to_pack = None
    
    # start timer of problem solve runtime    
    startTime = time.time()
    
    # run algorithm to determine items to pack
    items_to_pack = loadKnapsack(items,knapsack_cap)
    
    # calculate the time of program execution
    execTime = time.time() - startTime
    
    # if items_to_pack is correctly formatted, then proceed to checkCapacity
    if isinstance(items_to_pack,list):
        for this_key in items_to_pack:
            if this_key in items.keys():
                in_knapsack[this_key] = items[this_key]
                del items[this_key]

            # if one of the IDs in items_to_pack are not in the original problem ID, then output an error
            else:
                errors = True
                status = 'Problem ' + str(problem_id) + ' solution references invalid key'
                if not silent_mode:
                    print('Problem ' + str(problem_id) + ' solution references invalid key')

    # if items_to_pack is not a list, then output an error
    else:
        errors = True
        status = 'Problem ' + str(problem_id) + ' is not a list'
        if silent_mode:
            print(error_response_not_list)
    
    # if items_to_pack volume is at/under capacity, then output the result
    # (print statements below reorganized by me, and I also added a comparison to the optimal value)
    if errors == False:
        knapsack_ok = checkCapacity(in_knapsack,knapsack_cap)
        if knapsack_ok:
            knapsack_result = knapsack_value(in_knapsack)
            print('Problem ' + str(problem_id))
            print('Knapsack loaded within capacity')
            print('Knapsack value: ',str(knapsack_result))
            print('Percent of opt: ',round(knapsack_result/probData[problem_id]['opt'],4)*100,'%')
            print('Execution time: ',str(round(execTime,10)),' seconds\n')
            
    # if items_to_pack volume is over capacity, then output an error message
        else:
            print('Problem ' + str(problem_id) + ' knapsack overloaded')

    # if there was an error captured previously but not printed, it will be printed here
    else:
        print(status)



