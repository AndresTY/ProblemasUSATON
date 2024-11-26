#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'activityNotifications' function below.
#
# The function is expected to return an INTEGER.
# The function accepts following parameters:
#  1. INTEGER_ARRAY expenditure
#  2. INTEGER d
#

from bisect import insort, bisect_left

def median(sorted_window, d):
    # If d is odd, return the middle element
    # If d is even, return the average of the two middle elements
    if d % 2 == 1:
        return sorted_window[d // 2]
    else:
        return (sorted_window[d // 2] + sorted_window[d // 2 - 1]) / 2

def activityNotifications(expenditure, d):
    notifications = 0
    sorted_window = sorted(expenditure[:d])
    
    for i in range(d, len(expenditure)):
        # Calculate the median of the trailing d days
        med = median(sorted_window, d)
        
        # Check if notification is needed
        if expenditure[i] >= 2 * med:
            notifications += 1
        
        # Update the sorted window for the next day
        # Remove the element that is sliding out of the window
        old_value = expenditure[i - d]
        del sorted_window[bisect_left(sorted_window, old_value)]
        
        # Add the new element that comes into the window
        insort(sorted_window, expenditure[i])
        
    return notifications


if __name__ == '__main__':
   

    first_multiple_input = input().rstrip().split()

    n = int(first_multiple_input[0])

    d = int(first_multiple_input[1])

    expenditure = list(map(int, input().rstrip().split()))

    result = activityNotifications(expenditure, d)

    print(str(result))

   
