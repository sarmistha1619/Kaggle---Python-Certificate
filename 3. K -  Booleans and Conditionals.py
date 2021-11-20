#1.
#Many programming languages have sign available as a built-in function. Python doesn't, but we can define our own! In the cell below, define a function called sign which takes a numerical argument and returns -1 if it's negative, 1 if it's positive, and 0 if it's 0.
# Your code goes here. Define a function called 'sign'
def sign(x):
    if x > 0:
        return 1
    elif x < 0:
        return -1
    else:
        return 0
# Check your answer
q1.check()

#2.
#We've decided to add "logging" to our to_smash function from the previous exercise.
if total_candies == 1:
    print("Splitting 1 candy")
else:
    print("Splitting", total_candies, "candies")

print("Splitting", total_candies, "candy" if total_candies == 1 else "candies")

'''
3. 🌶️¶
In the tutorial, we talked about deciding whether we're prepared for the weather. I said that I'm safe from today's weather if...

I have an umbrella...
or if the rain isn't too heavy and I have a hood...
otherwise, I'm still fine unless it's raining and it's a workday
The function below uses our first attempt at turning this logic into a Python expression. I claimed that there was a bug in that code. Can you find it?

To prove that prepared_for_weather is buggy, come up with a set of inputs where either:

the function returns False (but should have returned True), or
the function returned True (but should have returned False).
To get credit for completing this question, your code should return a Correct result.
'''
def prepared_for_weather(have_umbrella, rain_level, have_hood, is_workday):
    # Don't change this code. Our goal is just to find the bug, not fix it!
    return have_umbrella or rain_level < 5 and have_hood or not rain_level > 0 and is_workday

# Change the values of these inputs so they represent a case where prepared_for_weather
# returns the wrong answer.
have_umbrella = True
rain_level = 0.0
have_hood = True
is_workday = True

# Check what the function returns given the current values of the variables above
actual = prepared_for_weather(have_umbrella, rain_level, have_hood, is_workday)
print(actual)

# Check your answer
q3.check()

'''
4.
The function is_negative below is implemented correctly - it returns True if the given number is negative and False otherwise.

However, it's more verbose than it needs to be. We can actually reduce the number of lines of code in this function by 75% while keeping the same behaviour.

See if you can come up with an equivalent body that uses just one line of code, and put it in the function concise_is_negative. (HINT: you don't even need Python's ternary syntax)
'''
def is_negative(number):
    if number < 0:
        return True
    else:
        return False

def concise_is_negative(number):
    pass # Your code goes here (try to keep it to one line!)

# Check your answer
q4.check()

'''
5a.
The boolean variables ketchup, mustard and onion represent whether a customer wants a particular topping on their hot dog. We want to implement a number of boolean functions that correspond to some yes-or-no questions about the customer's order. For example:
'''
def onionless(ketchup, mustard, onion):
    """Return whether the customer doesn't want onions.
    """
    return not onion
def wants_all_toppings(ketchup, mustard, onion):
    """Return whether the customer wants "the works" (all 3 toppings)
    """
    pass

# Check your answer
q5.a.check()

'''
5b.
For the next function, fill in the body to match the English description in the docstring.
'''
def wants_plain_hotdog(ketchup, mustard, onion):
    """Return whether the customer wants a plain hot dog with no toppings.
    """
    pass

# Check your answer
q5.b.check()

'''
5c.
You know what to do: for the next function, fill in the body to match the English description in the docstring.
'''
def exactly_one_sauce(ketchup, mustard, onion):
    """Return whether the customer wants either ketchup or mustard, but not both.
    (You may be familiar with this operation under the name "exclusive or")
    """
    pass

# Check your answer
q5.c.check()

'''
6. 🌶️
We’ve seen that calling bool() on an integer returns False if it’s equal to 0 and True otherwise. What happens if we call int() on a bool? Try it out in the notebook cell below.

Can you take advantage of this to write a succinct function that corresponds to the English sentence "does the customer want exactly one topping?"?
'''
def exactly_one_topping(ketchup, mustard, onion):
    """Return whether the customer wants exactly one of the three available toppings
    on their hot dog.
    """
    pass

# Check your answer
q6.check()


'''
7. 🌶️ (Optional)
In this problem we'll be working with a simplified version of blackjack (aka twenty-one). In this version there is one player (who you'll control) and a dealer. Play proceeds as follows:

The player is dealt two face-up cards. The dealer is dealt one face-up card.
The player may ask to be dealt another card ('hit') as many times as they wish. If the sum of their cards exceeds 21, they lose the round immediately.
The dealer then deals additional cards to himself until either:
the sum of the dealer's cards exceeds 21, in which case the player wins the round
the sum of the dealer's cards is greater than or equal to 17. If the player's total is greater than the dealer's, the player wins. Otherwise, the dealer wins (even in case of a tie).
When calculating the sum of cards, Jack, Queen, and King count for 10. Aces can count as 1 or 11 (when referring to a player's "total" above, we mean the largest total that can be made without exceeding 21. So e.g. A+8 = 19, A+8+8 = 17)

For this problem, you'll write a function representing the player's decision-making strategy in this game. We've provided a very unintelligent implementation below:
'''
def exactly_one_topping(ketchup, mustard, onion):
    """Return whether the customer wants exactly one of the three available toppings
    on their hot dog.
    """
    pass

# Check your answer
q6.check()


