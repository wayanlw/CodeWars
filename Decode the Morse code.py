# ---------------------------------- Mthod 1 --------------------------------- #

def decodeMorse(morse_code):
    finalstring = ''
    chars = ''
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
    '''
    Decoding using an array
    '''
    sent = []
    word = ''

    for splitWords in morse_code.strip().split('   '):
                                                 #splitting the morse code in to words by splitting using 3 spaces
        for splitchars in splitWords.split(' '):
                                                 ## splitting the most code in to characters by splitting using 1 space
            word = word + MORSE_CODE[splitchars] #adding the letters to the string
        sent.append(word)                        # adding to a string thinking of using ''.join() at the end
        word = ''                                # have to make a blank string. Else the previous words will be present.

    return ' '.join(sent)
