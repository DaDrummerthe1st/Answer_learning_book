def add_two_numbers(x: int, y=5: int) --> None:
    """Module is about adding the numbers
    >>> add_two_numbers(3)
    8
    >>> add_two_numbers(5, 2)
    7
    >>> add_two_numbers("torsdag")
    exception
    
    
    """
    try:
        if x == int or y == int:
            return x + y
    except SyntaxError as syntax_e:
        print("Syntax Error: " + str(syntax_e))
    except Exception as e:
        print("Unknown error: " + str(e))
    except:
        print("Even more unknown error!!!!")

def subtract_two_numbers(x, y=5):
    try:
        if x == int or y == int:
            return x - y
    except Exception as e:
        print("Unknown error: " + str(e))
    except:
        print("Even more unknown error!!!!")

