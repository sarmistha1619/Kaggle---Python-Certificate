#0
# Check your answer
color="red"
q0.check()

#1
pi = 3.14159 # approximate
diameter = 3

# Create a variable called 'radius' equal to half the diameter
radius=diameter/2

# Create a variable called 'area', using the formula for the area of a circle: pi times the radius squared
area=pi*radius*radius
#/area = pi * radius ** 2

# Check your answer
q1.check()

#2
########### Setup code - don't touch this part ######################
# If you're curious, these are examples of lists. We'll talk about
# them in depth a few lessons from now. For now, just know that they're
# yet another type of Python object, like int or float.
a = [1, 2, 3]
b = [3, 2, 1]
q2.store_original_ids()
######################################################################

# Your code goes here. Swap the values to which a and b refer.
# If you get stuck, you can always uncomment one or both of the lines in
# the next cell for a hint, or to peek at the solution.
a,b=b,a
######################################################################

# Check your answer
q2.check()

'''
#another solution:
tmp = a
a = b
b = tmp
'''
#3a.
#Add parentheses to the following expression so that it evaluates to 1.
#5 - 3 // 2
(5 - 3) // 2

#3b.
#Questions, like this one, marked a spicy pepper are a bit harder. Add parentheses to the following expression so that it evaluates to 0.
#8 - 3 * 2 - 1 + 1
8 - (3 * 2) - (1 + 1)

#4.
#Alice, Bob and Carol have agreed to pool their Halloween candy and split it evenly among themselves. For the sake of their friendship, any candies left over will be smashed. For example, if they collectively bring home 91 candies, they'll take 30 each and smash 1. Write an arithmetic expression below to calculate how many candies they must smash for a given haul.
# Variables representing the number of candies collected by alice, bob, and carol
a=alice_candies = 121
b=bob_candies = 77
c=carol_candies = 109

# Your code goes here! Replace the right-hand side of this assignment with an expression
# involving alice_candies, bob_candies, and carol_candies
t=to_smash = -1
print((a+b+c)%3)
# Check your answer
q4.check()



