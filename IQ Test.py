
"""
Bob is preparing to pass IQ test. The most frequent task in this test is to find out which one of the given numbers differs from the others. Bob observed that one number usually differs from the others in evenness. Help Bob — to check his answers, he needs a program that among the given numbers finds one that is different in evenness, and return a position of this number.

! Keep in mind that your task is to help Bob solve a real IQ test, which means indexes of the elements start from 1 (not 0)
"""
def iq_test(numbers):
    odd = 0
    even = 0
    oddPlc = 0
    evenPlc = 0
    for i,number in enumerate(numbers.split()):
        if int(number)%2 == 0:
            even+=1
            evenPlc = i+1
        else:
            odd+=1
            oddPlc = i+1

    return(oddPlc if odd<even else evenPlc)

print(iq_test("1 2 2"))