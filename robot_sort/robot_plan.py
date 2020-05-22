Understand, plan, & implement the Robot Sort algorithm (6 points)

You have been given a robot with very basic capabilities:

It can move left or right.
It can pick up an item
If it tries to pick up an item while already holding one, it will swap the items instead.
It can compare the item it's holding to the item in front of it.
It can switch a light on its head on or off.
Your task is to program this robot to sort lists using ONLY these abilities.

Rules

You may use any pre-defined robot methods.
You may NOT modify any pre-defined robot methods.
You may use logical operators. (if, and, or, not, etc.)
You may use comparison operators. (>, >=, <, <=, ==, is, etc.)
You may use iterators. (while, for, break, continue)
You may NOT store any variables. (=)
You may NOT access any instance variables directly. (self._anything)
You may NOT use any Python libraries or class methods. (sorted(), etc.)
You may define robot helper methods, as long as they follow all the rules.

Hints

Come up with a plan and write out your algorithm before coding. If your plan is sound but you don't reach a working implementation in three hours, you may receive partial credit.

There is no efficiency requirement but you may lose points for an unreasonably slow solution. Tests should run in far less than 1 second.

We discussed a sorting method this week that might be useful. Which one? My guess is bubble sort. 

The robot has exactly one bit of memory: its light. Why is this important?

# Can Move Right Plan
    # determine that there is length to be moved along meaning robot it not in a tight space like a closet with no room to move.
    # assuming the robot is in a position, the length has to be greater than 1 and he would have to be in the 1st position or index 0 to be able to move right if the length is only 2.
    # if the length is greater than 2, the robot could be in slot one, two, and so on to be able to move right. Unless the robot is at index(-1), he cannot move right either as the array is finished.
    # find the position and give the conditionals 

# Can Move Left Plan
    # determine that there is length to be moved along meaning robot it not in a tight space like a closet with no room to move.
    # assuming the robot is in a position, the length has to be greater than 1 and he would have to be in the 2nd position or index 1 to be able to move left if the length is only 2.
    # if the length is greater than 2, the robot just can't be in index 0 to move left. He can be in any other position.
    # find the position and give the conditionals 

# Move Right Plan
    # If the robot is able to move right (meaning length of space and or position of robot is appropriate for moving right), incrememnt the position by 1 and return true
    # else return false and do not incrememnt position


# Move Left Plan
    # If the robot is able to move left (meaning length of space and or position of robot is appropriate for moving left), decrease the position by 1 and return true
    # else return false and do not decrease position


# Swap Item Plan
    # Since Robot memory is one, the length of what the robot can hold is one. So, if the length is 1, the robot will swap (take the item from the array and replace the previous item back to the array). If the length is 0, the robot will pickup the item. 


# Compare Item Plan
    # While Comparing, get the value of the item in hand and the item in front(item directly to left of item in hand) of the robot. Return 1 for if in hand value is larger, -1 if in hand value is less, 0 if both values are =. 


# Set Light On Plan
    # Determine if switch exists. If exists, add 1. if not, return none. If already set to one, return light/add none


# Set Light Off Plan
    # Determine if switch exists. If exists, and position is 1, subtract 1. If position is 0, return light/subtract none


#  Light On Plan
    # If light is set to off, hit switch. switch runs set light on function


# Sort Plan
    # compare 2 indices at a time and switch them as necessary if one i larger than the other. So for example, if indices 2 & 3 are 7, 4, switch them to 4, 7 and continue to loop through the array doing this. Continue this until it is completed. 