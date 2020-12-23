"""
Using decorators in python for automatic registration

https://web.archive.org/web/20200218115053/http://scottlobdell.me/2015/08/using-decorators-python-automatic-registration/

The problem to solve:

Animals abstract class - new animal to be integrated to the environment -
"""

from .abstract_animal import AbstractAnimal
from .class_registry import registered_class, REGISTERED_CLASSES

class OldDog(AbstractAnimal):
    def do_something_important(self):
        print("Do some old dog specific logic")


class OldCat(AbstractAnimal):
    def do_something_important(self):
        print('Do some old cat specific logic')




@registered_class
class Dog(AbstractAnimal):
    def do_something_important(self):
        pass
        #print('Do some dog specific logic')

@registered_class
class Cat(AbstractAnimal):
    def do_something_important(self):
        print('Do some cat specific logic')



def test():
    ALL_ANIMAL_CLASSES = {
        OldDog,
        OldCat
    }

    for animal_cls in ALL_ANIMAL_CLASSES:
        animal_cls().do_something_important()

    """
    Notice how in the above example how a developer must:
    1) create a new subclass
    2) add it to the list of existing animal classes

    We should get rid of the second step.

    @app.route('/hello')
    def hello():
        return 'Hello World'
    """

    # for animal_cls in REGISTERED_CLASSES:
    #     print(animal_cls().do_something_important())
    d = Dog()
    print(d.do_something_important())


if __name__ == '__main__':
    test()
