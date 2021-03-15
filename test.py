"""
Write a function that takes a string of braces, and determines if the order of the braces is valid. It should return true if the string is valid, and false if it's invalid.

This Kata is similar to the Valid Parentheses Kata, but introduces new characters: brackets [], and curly braces {}. Thanks to @arnedag for the idea!

All input strings will be nonempty, and will only consist of parentheses, brackets and curly braces: ()[]{}.

What is considered Valid?
A string of braces is considered valid if all braces are matched with the correct brace.

Examples
"(){}[]"   =>  True
"([{}])"   =>  True
"(}"       =>  False
"[(])"     =>  False
"[({})](]" =>  False
"""



# --------------------------------- My answer -------------------------------- #

def validBraces(string):
    state = True
    stack = []
    dicParan = {"(":")", "[":"]", "{":"}"}
    for paran in string:
        if paran in dicParan.keys():
            stack.append(paran)
        elif paran in dicParan.values() and stack:
            if dicParan[stack[-1]] == paran:
                stack.pop()
            else:
                state = False
                break
        else:
            state = False
            break
    if len(stack)!=0:
        state=False
    return state

print (validBraces(")(}{]["))

# ---------------------------------- Others ---------------------------------- #

def validBraces(string):
    braces = {"(": ")", "[": "]", "{": "}"}
    stack = []
    for character in string:
        if character in braces.keys():
            stack.append(character)
        else:
            if len(stack) == 0 or braces[stack.pop()] != character:
                return False
    return len(stack) == 0


# ---------------------------------------------------------------------------- #


def validBraces(string):

  while '()' in string or '[]' in string or '{}' in string:
       string = string.replace('{}','')
       string = string.replace('()','')
       string = string.replace('[]', '')

  return not string


