"""List of prime numbers generator."""
"""ENTER YOUR SOLUTION HERE!"""

def is_Prime(num):
    if num == 1 or num == 2:
        return True
    elif num == 4:
        return False
    
    for i in range(2, num//2):
        if num%i == 0:
            return False
    return True

def primes(number_of_primes):
    if number_of_primes <= 0:
        raise ValueError("Value input is less than or equal to 0.")

    list = []

    current_val = 2
    while number_of_primes > len(list):
        if is_Prime(current_val):
            list.append(current_val)
        current_val +=1

    return list