"""
Collect|
Write a function that takes a string of parentheses, and determines if the order of the parentheses is valid. The function should return true if the string is valid, and false if it's invalid.

Examples
"()"              =>  true
")(()))"          =>  false
"("               =>  false
"(())((()())())"  =>  true
"""
# -------------------------------- my solution ------------------------------- #

def valid_parentheses(string):
    paran = []
    for i in string:
        if i =='(' or i== ')':
            paran.append(i)
    finString = ''.join(paran)

    while '()' in finString:
        finString = finString.replace('()','')

    return not finString

print (valid_parentheses('p(tdms)qgz(tc(rx)nk)v()f'))
sorted()

# --------------------------------- option 2 --------------------------------- #
def valid_parentheses(string):
    cnt = 0
    for char in string:
        if char == '(': cnt += 1
        if char == ')': cnt -= 1
        if cnt < 0: return False
    return True if cnt == 0 else False