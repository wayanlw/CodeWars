import re

def generate_hashtag(s):
    if s=='': return False

    finString = []
    cleanString = re.sub(' +',' ',s.strip())
    cleanString = cleanString.title()
    if cleanString[0] != '#':
        finString.append('#')
    for i,char in enumerate(cleanString):
        if char != ' ':
            finString.append(char)

    if len(finString) > 140: return False
    return ''.join(finString)


print(generate_hashtag('   Hello     World   '))