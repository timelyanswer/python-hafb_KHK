#!/usr/bin/env python3
"""
Author : t11 <me@wsu.com>
Date   : 8/12/2021
Purpose: basics of decorators
"""

def outer_function(msg):
    message = msg
    def inner_function():
        print(message)

    return inner_function

def decorator_function(original_function):
    def wrapper_function(*args, **kwargs):
        print(f'wrapper executed this before {original_function.__name__}')
        return original_function(*args, **kwargs)      # the execution of the function
    return wrapper_function

@decorator_function
def display():
    print(f'display function ran')



# --------------------------------------------------
def main():
    """Make your noise here"""
    hi_func = outer_function('hi')
    bye_func = outer_function('bye')
    hi_func()
    bye_func()

    # without decorator
    decorated_display = decorator_function(display)
    decorated_display()

    # with decorator
    display()







# --------------------------------------------------
if __name__ == '__main__':
    main()
