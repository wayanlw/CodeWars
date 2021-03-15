
# ---------------------------------------------------------------------------- #
#                                 Which are in?                                #
# ---------------------------------------------------------------------------- #

# -------------------------- my answer without a set ------------------------- #

def in_array(array1, array2):
    stack = []
    for item1 in array1:
        for item2 in array2:
            if item1 in item2 and item1 not in stack:
                stack.append(item1)
                break

    return sorted(stack)

# -------------------------------- using a set ------------------------------- #

def in_array(array1, array2):
    stack = set()
    for item1 in array1:
        for item2 in array2:
            if item1 in item2:
                stack.add(item1)
                break

    return sorted(stack)


a1 = ["live", "arp", "strong"]
a2 = ["lively", "alive", "harp", "sharp", "armstrong"]

print(in_array(a1,a2))