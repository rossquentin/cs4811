# submission.py
# ----------------
# Attribution Information: This part of the project was adapted from CS221 and 
# the PacMan Projects. 
# For the PacMan Projects: 
# Licensing Information:  You are free to use or extend these projects for
# educational purposes provided that (1) you do not distribute or publish
# solutions, (2) you retain this notice, and (3) you provide clear
# attribution to UC Berkeley, including a link to http://ai.berkeley.edu.
# 
# Attribution Information: The Pacman AI projects were developed at UC Berkeley.
# The core projects and autograders were primarily created by John DeNero
# (denero@cs.berkeley.edu) and Dan Klein (klein@cs.berkeley.edu).
# Student side autograding was added by Brad Miller, Nick Hay, and
# Pieter Abbeel (pabbeel@cs.berkeley.edu).
# 08-2020


from __future__ import print_function
import math
import collections
import shop


############################################################
# Question 1 - addition 

def add(a, b):
    "Return the sum of a and b"
    "*** YOUR CODE HERE ***"
    # BEGIN_YOUR_CODE 
    return a + b
    # END_YOUR_CODE


############################################################
# Question 2 - buyLotsOfFruit 
fruitPrices = {'apples': 2.00, 'oranges': 1.50, 'pears': 1.75,
               'limes': 0.75, 'strawberries': 1.00}


def buyLotsOfFruit(orderList):
    """
        orderList: List of (fruit, numPounds) tuples

    Returns cost of order. If some fruit is not in list, print an error 
    message and return None.
    """
    totalCost = 0.0
    "*** YOUR CODE HERE ***"
    # BEGIN_YOUR_CODE
    for fruit, numPounds in orderList:
        if fruit not in fruitPrices:
            print("error: fruit not found")
            return None
        totalCost += numPounds * fruitPrices[fruit]
    return totalCost
    # END_YOUR_CODE


############################################################
# Question 3 - shopSmart 

def shopSmart(orderList, fruitShops):
    """
        orderList: List of (fruit, numPound) tuples
        fruitShops: List of FruitShops

    Return the FruitShop where your order costs the least.
    """
    "*** YOUR CODE HERE ***"
    # BEGIN_YOUR_CODE
    best = fruitShops[0]
    cheapest = best.getPriceOfOrder(orderList)

    for shop in fruitShops[1:]:
        cost = shop.getPriceOfOrder(orderList)
        if cost < cheapest:
            best = shop
            cheapest = cost

    return best
    # END_YOUR_CODE


############################################################
# Question 4 - findAlphabetLastWord 

def findAlphabetLastWord(text):
    """
    Given a string |text|, return the word in |text| that comes last
    alphabetically (that is, the word that would appear last in a dictionary).
    A word is defined by a maximal sequence of characters without whitespaces.
    You might find max() and list comprehensions handy here.
    """
    "*** YOUR CODE HERE ***"
    # BEGIN_YOUR_CODE (our solution is 1 line of code, but don't worry if you deviate from this)
    return max(text.split())
    # END_YOUR_CODE


############################################################
# Question 5 - euclideanDistance 

def euclideanDistance(loc1, loc2):
    """
    Return the Euclidean distance between two locations, where the locations
    are pairs of numbers (e.g., (3, 5)).
    """
    "*** YOUR CODE HERE ***"
    # BEGIN_YOUR_CODE (our solution is 1 line of code, but don't worry if you deviate from this)
    return math.sqrt((loc1[0] - loc2[0]) ** 2 + (loc1[1] - loc2[1]) ** 2)
    # END_YOUR_CODE


############################################################
# Question 6 - findSingletonWords

def findSingletonWords(text):
    """
    Splits the string |text| by whitespace and returns the set of words that
    occur exactly once.
    If no singleton words exist return the emptyset.
    """
    "*** YOUR CODE HERE ***"
    # BEGIN_YOUR_CODE (our solution is 4 lines of code, but don't worry if you deviate from this)
    count = collections.defaultdict(int)
    for word in text.split():
        count[word] += 1
    return set([
        word for word, count in count.items()
        if count is 1])
    # END_YOUR_CODE


############################################################
# Question 7 - lenLongestPalindrome

def lenLongestPalindrome(text):
    """
    A palindrome is a string that is equal to its reverse (e.g., 'ana'). 
    Computer the length of the longest palindrome that can be obtained by 
    deleting letters from text. 
    Do not try a brute force approach on this function.  Your algorithm should 
    run in O(len(text)^2) time. 
    Consider defining a recurrence before you begin coding. 
    """
    "*** YOUR CODE HERE ***"
    # BEGIN_YOUR_CODE
    if len(text) <= 1:
        return len(text)
    return getLongestPalindromeLength(text, {}, 0, len(text)-1)
    #return getLongestPalindromeLengthCacheless(text, 0, len(text) - 1)
    # END_YOUR_CODE


############################################################
#  Extra Functions you may want to define


def getLongestPalindromeLengthCacheless(text, i, j):
    if i is j:
        return 1
    # last 2 characters the same
    elif text[i] == text[j] and (j == i + 1):
        return 2
    # first and last character the same, get the longest palindrome of subtext. add 2
    elif text[i] == text[j]:
        return getLongestPalindromeLengthCacheless(text, i + 1, j - 1) + 2
    # first and last character not the same. split into two attempts
    else:
        return max(getLongestPalindromeLengthCacheless(text, i + 1, j),
                   getLongestPalindromeLengthCacheless(text, i, j - 1))


def getLongestPalindromeLength(text, cache, i, j):
    # single character
    if i is j:
        return 1
    # last 2 characters the same
    elif text[i] == text[j] and (j == i + 1):
        return 2
    # first and last character the same, get the longest palindrome of subtext. add 2
    elif text[i] == text[j]:
        s = text[i + 1:j]
        if s not in cache:
            cache[s] = getLongestPalindromeLength(text, cache, i + 1, j - 1)
        return cache[s] + 2
    # first and last character not the same. split into two attempts
    else:
        s1 = text[i:j]
        s2 = text[i + 1:j + 1]
        if s1 not in cache:
            cache[s1] = getLongestPalindromeLength(text, cache, i, j - 1)
        if s2 not in cache:
            cache[s2] = getLongestPalindromeLength(text, cache, i + 1, j)
        return max(cache[s1], cache[s2])
