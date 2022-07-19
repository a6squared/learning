def string_formatting():
    # Learn about string-formatting and escape sequences
    return 'Twinkle, twinkle, little star,\n\tHow I wonder what you are!\n\t\tUp above the world so high,\n\t\tLike a diamond in the sky.\nTwinkle, twinkle, little star,\n\t\tHow I wonder what you are'


def current_version():
    # Use the 'sys' library to learn about the computer you're using.
    import sys
    result = sys.version
    return result


def area_of_circle(radius):
    # Use multiplication to solve a problem. Assume Pi is 3.14.
    # Challenge: Use a variable
    x = float(3.14)
    result =  (x) * (radius**2)

    return result


def file_extension(param):
    x = param.split('.')
    # Demonstrate how to split a string using the 'str' Built-in Type
    result= (x[1])
    # Learn to access an element from the 'list' Built-in Type
    return result


def get_builtin_docs():
    # Recall the 3 components of a Python "Object"
    # Use a "dunder" function to access an object attribute.
    # Hint: Use x.__doc__
    return ''
