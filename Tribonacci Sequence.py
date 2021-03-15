def tribonacci(signature,n):
    if n == 0:
        signature = []
    elif n<=2:
        signature = signature[:n]
    else:
        for i in range(n-3):
            # newElem=sum(signature[-3:])
            signature.append(sum(signature[-3:]))
    return (signature)

print (tribonacci([1, 1, 1], 4))
