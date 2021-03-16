import math

def is_prime(num):
    """
    Property:
        Every number n that is not prime has at least one prime divisor p
        such 1 < p < square_root(n)
    """
    if num ==2     :return True
    if num % 2 == 0:return False
    if num <=1     :return False

    if isinstance(num,int):
        for i in range(2, int(math.sqrt(num))+1):
            if (num % i)==0:
                return False
                break
        return True
    return False

print(is_prime(9))