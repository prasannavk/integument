import time

def timetest(input_func):

    def timed(*args, **kwargs):
        start_time = time.time()
        result = input_func(*args, **kwargs)
        end_time = time.time()
        print("Method Name - {0},"
              "Args - {1},"
              "KWArgs - {2},"
              "Execution Time - {3}".format(
            input_func.__name__,
            args,
            kwargs,
            end_time - start_time
        ))
        return result
    return timed

@timetest
def foobar(*args, **kwargs):
    time.sleep(0.3)
    print("inside foobar")
    print(args, kwargs)


foobar(["hello, world"], foo=2, bar=5)

'''

M  E  T  H  O  D      D  E C O R A T O R

'''
def method_decorator(method):

    print('method is ', method)
    def inner(city_instance):
        if city_instance.name == "SFO":
            print('It\'s a cool place to live in')
        else:
            method(city_instance)

    return inner


class City:
    def __init__(self, name):
        self.name = name

    @method_decorator
    def print_test(self):
        print(self.name)

p1 = City("SFO")
p1.print_test()


'''

C L A S S   D E C O R A T O R S 

If you want the decorator to return a custom object that does something different
to what a function does, then a class decorator should be used.

With a class, you can add methods and properties to the decorated callable object,
or implement operations on them.
'''
class DecoClass:
    def __init__(self, f):
        self.f = f


    def __call__(self, *args, **kwargs):
        # before f actions
        print('decorator initialized')
        self.f(*args, **kwargs)
        print('decorator terminated')
        # after f actions

@DecoClass
def klass(inp):
    print('class' + inp)

x = klass
print(x.f)
klass(' podra')


'''
  C  H  A  I  N  I  N  G           D  E  C  O  R  A  T  O  R  S
  

when you chain decorators, the order in which they are stacked is bottom to top.
'''

def makebold(f):
    return lambda: "<b>" + f() + "</b>"

def makeitalic(f):
    return lambda: "<i>" + f() + "</i>"

@makebold
@makeitalic
def say():
    return "hello"

print(say())

'''
Functools and wraps
'''
def decorator(func):
    """decorator docstring"""
    def inner_function(*args, **kwargs):
        """
        inner function docstring
        """
        print(func.__name__ + " was called")
        return func(*args, **kwargs)
    return inner_function

@decorator
def foobar(x):
    """
    foobar docstring
    :param x:
    :return:
    """
    return x**2

print(foobar.__name__)
print(foobar.__doc__)

from functools import wraps

# this time we are able to keep the original docstring and original func name
def wrapped_decorator(func):
    """wrapped decorator docstring"""
    @wraps(func)
    def inner_function(*args, **kwargs):
        """
        inner function docstring
        """
        print(func.__name__ + " was called")
        return func(*args, **kwargs)
    return inner_function

@wrapped_decorator
def foobar(x):
    """
    foobar docstring
    :param x:
    :return:
    """
    return x**2

print(foobar.__name__)
print(foobar.__doc__)


'''
Decorators with Arguments
'''
def decorator(arg1, arg2):

    def inner_function(function):
        @wraps(function)
        def wrapper(*args, **kwargs):
            print('Arguments passed to decorator are %s and %s' % (arg1, arg2))
            function(*args, **kwargs)

        return wrapper
    return inner_function


@decorator("aaaarg1", "bbbbarg2")
def print_args(*args):
    for arg in args:
        print(arg)

print_args(1, 2, 3)


class ClassDecorator:
    def __init__(self, arg1, arg2):
        print('Arguments passed to ClassDecorator %s and %s' % (arg1, arg2))
        self.arg1 = arg1
        self.arg2 = arg2

    def __call__(self, foo, *args, **kwargs):
        def inner_func(*args, **kwargs):
            print('Decorated function args %s and %s' % (self.arg1, self.arg2))
            return foo(*args, **kwargs)

        return inner_func

@ClassDecorator("arg1", "arg2")
def print_args(*args):
    for arg in args:
        print(arg)

print_args(1, 2, 3)