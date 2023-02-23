from abc import abstractmethod

class A:
    def methBase(self):
        print('methBase')

    @abstractmethod
    def draw(self):
        pass


class B(A):
    def draw(self):
        print('drowB')


class C(A):
    def draw(self):
        print('drowC')


class AFactory:
    def __init__(self, endpoint):
        self.__class_type__ = endpoint
    def BuildA(self )-> A:
        if (self.__class_type__ == "B"):
            return B()
        return C()
