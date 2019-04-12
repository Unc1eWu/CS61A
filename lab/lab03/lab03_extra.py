""" Optional problems for Lab 3 """

# Q4
def is_prime(n):
    """Returns True if n is a prime number and False otherwise.

    >>> is_prime(2)
    True
    >>> is_prime(16)
    False
    >>> is_prime(521)
    True
    """
    "*** YOUR CODE HERE ***"
    def calculate(i):
        if i < n:
            if n % i == 0:  # 'n ** 0.5' could be replaced by 'n'
                return False
            else:
                return calculate(i + 1)
        else:
            return True
    return calculate(2)

# Q5
def gcd(a, b):
    """Returns the greatest common divisor of a and b.
    Should be implemented using recursion.

    >>> gcd(34, 19)
    1
    >>> gcd(39, 91)
    13
    >>> gcd(20, 30)
    10
    >>> gcd(40, 40)
    40
    """
    "*** YOUR CODE HERE ***"
    if a < b:
        return gcd(b, a)
    elif a % b == 0:
        return b
    else:
        return gcd(b, a % b)

# Q6
def ten_pairs(n):
    """Return the number of ten-pairs within positive integer n.

    >>> ten_pairs(7823952)
    3
    >>> ten_pairs(55055)
    6
    >>> ten_pairs(9641469)
    6
    """
    "*** YOUR CODE HERE ***"
    if n < 10:
        return 0
    else:
        return ten_pairs(n // 10) + count_digit(n // 10, 10 - n % 10)

def count_digit(n, digit):
    if n == 0:
        return 0
    elif n % 10 == digit:
        return count_digit(n // 10, digit) + 1
    else:
        return count_digit(n // 10, digit)

# Q7
def factors_list(n):
    """Return a list containing all the numbers that divide `n` evenly, except
    for the number itself. Make sure the list is in ascending order.

    >>> factors_list(6)
    [1, 2, 3]
    >>> factors_list(8)
    [1, 2, 4]
    >>> factors_list(28)
    [1, 2, 4, 7, 14]
    """
    all_factors = []
    "*** YOUR CODE HERE ***"
    def calculate(i):
        if i < n and n % i == 0:
            all_factors.append(i)
        if i < n:
            calculate(i + 1)
    calculate(1)
    return all_factors

