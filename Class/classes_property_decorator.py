class person:
    def __init__(self):
        self.__name=''

    @property
    def name(self):
        return self.__name
    @name.setter
    def name(self,name):
        self.__name=name

    @name.deleter
    def name(self):
        del self.__name

if __name__ == '__main__':
    p1 =person()
    print('Initial EMployee Name-'+p1.name)
    p1.name='John Smith'
    print('After EMployee Name-'+p1.name)
    print(p1.name)

    del p1.name
    print('After delete EMployee Name-' + p1.name)
