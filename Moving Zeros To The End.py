"""



"""




def move_zeros(array):
    non_zeros = []
    zeros = []

    for num in array:
        if num == 0:
            zeros.append(num)
            continue
        non_zeros.append(num)

    return (non_zeros+zeros)