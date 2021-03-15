"""
This time no story, no theory. The examples below show you how to write function accum:

Examples:

accum("abcd") -> "A-Bb-Ccc-Dddd"
accum("RqaEzty") -> "R-Qq-Aaa-Eeee-Zzzzz-Tttttt-Yyyyyyy"
accum("cwAt") -> "C-Ww-Aaa-Tttt"

"""

# --------------------------------- my answer -------------------------------- #

def accum(s):
    finalString = []
    for i,letter in enumerate(s):
        finalString.append(letter.upper()+letter.lower()*(i))
    return '-'.join(finalString)

print (accum("EvidjUnokmM"))


# ------------------------------- Better Answer ------------------------------ #

def accum(s):
    return '-'.join((a * i).title() for i, a in enumerate(s, 1))