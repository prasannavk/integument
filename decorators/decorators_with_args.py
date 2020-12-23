def decorator_fun(func):
    print('Inside decorator')

    def inner(*args, **kwargs):
        print('Inside inner function')
        print('Decorated the function')

        # do operations with func
        func()

    return inner

@decorator_fun
def func_to():
    print('Inside actual function')

func_to()

print('\n\n\nDecorator with kwargs')
def decorator(*args, **kwargs):
    print('Inside decorator')

    def inner(func):
        # code functionality here
        print('Inside inner function')
        print('I like', kwargs['like'])

        func()

    # returning inner function
    return inner

@decorator(like='beavers')
def my_func():
    print('Inside actual func')


print('\n\nDecorator with Active args for internal func')
'''
Now with active arguments
'''
def decorator_func(x, y):

    def Inner(func):
        def wrapper(*args, **kwargs):
            print('I like Geeksforgeeks')
            print('Summation of values - {}'.format(x+y))

            func(*args, **kwargs)

        return wrapper

    return Inner

# Not using decorator
def my_func(*args):
    for ele in args:
        print(ele)

decorator_func(12, 15)(my_func)('Geeks', 'fur', 'Greeks')