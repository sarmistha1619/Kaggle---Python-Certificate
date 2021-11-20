#1.
#Complete the body of the following function according to its docstring.
#HINT: Python has a built-in function round.
def round_to_two_places(num):
    """Return the given number rounded to two decimal places.

    >>> round_to_two_places(3.14159)
    3.14
    """
    # Replace this body with your own code.
    # ("pass" is a keyword that does literally nothing. We used it as a placeholder
    # because after we begin a code block, Python requires at least one line of code)

    return round(num, 2)


# Check your answer
q1.check()

#2
#The help for round says that ndigits (the second argument) may be negative. What do you think will happen when it is? Try some examples in the following cell.
'''
 As you've seen, ndigits=-1 rounds to the nearest 10, ndigits=-2 rounds to the nearest 100 and so on. Where might this be useful? Suppose we're dealing with large numbers:

The area of Finland is 338,424 km²
The area of Greenland is 2,166,086 km²

We probably don't care whether it's really 338,424, or 338,425, or 338,177. All those digits of accuracy are just distracting. We can chop them off by calling round() with ndigits=-3:

The area of Finland is 338,000 km²
The area of Greenland is 2,166,000 km²

(We'll talk about how we would get the commas later when we talk about string formatting :))
'''

#3.
#In the previous exercise, the candy-sharing friends Alice, Bob and Carol tried to split candies evenly. For the sake of their friendship, any candies left over would be smashed. For example, if they collectively bring home 91 candies, they'll take 30 each and smash 1. Below is a simple function that will calculate the number of candies to smash for any number of total candies.Modify it so that it optionally takes a second argument representing the number of friends the candies are being split between. If no second argument is provided, it should assume 3 friends, as before. Update the docstring to reflect this new behaviour.
def to_smash(total_candies, n_friends=3):
    return total_candies % n_friends

#4.
'''
It may not be fun, but reading and understanding error messages will be an important part of your Python career.

Each code cell below contains some commented buggy code. For each cell...

Read the code and predict what you think will happen when it's run.
Then uncomment the code and run it to see what happens. (Tip: In the kernel editor, you can highlight several lines and press ctrl+/ to toggle commenting.)
Fix the code (so that it accomplishes its intended purpose without throwing an exception)
'''
x = -10
y = 5
# Which of the two variables above has the smallest absolute value?
smallest_abs = min(abs(x, y))
def f(x):
 y = abs(x)
 return y
print(f(5))
