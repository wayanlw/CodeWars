# ---------------------------------------------------------------------------- #
#                             convert to camel case                             #
# ---------------------------------------------------------------------------- #

# ----------------------------- my first solution ---------------------------- #

def to_camel_case(text):
    #your code here
    # ret = [x.title() for x in text.replace("-","_").split("_")]
    finalstr = []
    ret = text.replace("-","_").split("_")
    for i,word in enumerate(ret):
        if i==0:
            finalstr.append(word)
            continue
        finalstr.append(word.title())
    return ''.join(finalstr)



text = "the_stealth_warrior"
print (to_camel_case(text))

# ---------------------------- my better solution ---------------------------- #

def to_camel_case(text):
    seperated = text.replace("-","_").split("_") # seperating text
    return (seperated[0] + ''.join([x.title() for x in seperated[1:]]))




