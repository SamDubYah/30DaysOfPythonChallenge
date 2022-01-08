#!/usr/bin/env python3


def middleList(input_list):
    middle = float(len(input_list)/2)
    if middle %2 != 0: # If length of list is odd, print both sides
        return input_list[int(middle)]
    else: 
        return input_list[int(middle) - 1], input_list[int(middle)]


# 1. Divide the countries list into two equal lists if it is even if not one more country for the first half.
def splitList(input_list):
    mid_ele = middleList(input_list) # Git the mid points
    
    if type(mid_ele) == tuple:
        # First half of list, from 0th ele to index of mid_ele + 1 --- adding 1 to include mid_ele
        first_half = input_list[:input_list.index(mid_ele[0])+1]
        second_half = input_list[input_list.index(mid_ele[1]):] # Start from second mid_ele to ned

        return first_half, second_half
        
    else:
        #Same reasoning as above, +1 to include element
        first_half = input_list[:input_list.index(mid_ele) + 1]
        second_half = input_list[input_list.index(mid_ele)+1:] # Adding 1 here to not include mid_ele

        return first_half, second_half
