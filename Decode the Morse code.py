# ---------------------------------- Mthod 1 --------------------------------- #

def decodeMorse(morse_code):
    finalstring = ''
    chars =''
    for splitWords in morse_code.strip().split('   '):
        for splitchars in splitWords.split(' '):
            chars = chars + MORSE_CODE[splitchars]
        if len(finalstring):
            finalstring = finalstring+' '+chars
        else:
            finalstring = finalstring+chars
        chars = ''
    return finalstring


# --------------------------------- methond 2 -------------------------------- #

def decodeMorse(morse_code):
    sent=[]
    word =''

    for splitWords in morse_code.strip().split('   '):
        for splitchars in splitWords.split(' '):
            word = word + MORSE_CODE[splitchars]
        sent.append(word)
        word = ''

    return ' '.join(sent)