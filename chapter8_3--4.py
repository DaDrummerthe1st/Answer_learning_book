# 3
### Skriv ett kodexempel där du fångar en exception. Endast din kreativitet sätter gränser.
def dived_by_zero_to_raise_exception(a, b=0):
    try:
        answer = a / b
    except ZeroDivisionError:
        return "can't divide by 0, which is the default"
    else:
        return (f"You made it work! The answer is: " + str(answer))

print(dived_by_zero_to_raise_exception(0))
print(dived_by_zero_to_raise_exception(5, b=123))

# 4
# Skapa en funktion add_two_small_numbers som adderar två tal.
# Om något av talen är större än 100 så skall du lyfta en exception
# och skriva ut meddelandet “both numbers must be smaller than or equal to 100”.
class Above100Exception(BaseException):
    ...


def add_two_small_numbers(a: int, b: int) -> int:
    """Adds two numbers (a, b)
    >>> print(add_two_small_numbers(6000, 23))
    >>> print(add_two_small_numbers(14,6))
    >>> print(add_two_small_numbers("tisdag", 6))
    """
    try:
        if a > 100 or b > 100:
            raise Above100Exception('both numbers must be smaller than or equal to 100')
    except TypeError as typeErr:
        return "an error in typing occured: " + str(typeErr)
    except Above100Exception as above100:
        return above100
    except:
        return "general exception ocured " + str(Exception)
    else:
        return a + b
    
print(add_two_small_numbers(14, 6))
print(add_two_small_numbers("tisdag", 6))
print(add_two_small_numbers(6000, 23))