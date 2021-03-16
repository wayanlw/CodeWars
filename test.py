# import re

# def valid_parentheses(string):
#     #your code here
#     while re.search('\(.*?\)',string):
#         string = re.sub('\(.*?\)','',string,1)
#         print (string)
#     print ("final String ", string)

#     if '(' in string: return False
#     if ')' in string: return False
#     return True

#     # return not ('(' in string or ')' in string)

# print (valid_parentheses(''))

import re

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
