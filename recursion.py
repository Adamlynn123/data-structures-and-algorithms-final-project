# create the sum recursion formula
def sum_recursion(n):
    # base case
    if n <= 0:
        return 0

    # use recursion to call function again and add to current number.
    else:
        return sum_recursion(n-1) + n

print(sum_recursion(10)) #55                                                    