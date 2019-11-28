class person:
    def __init__(self):
        self.__name=''
    def set_name(self,name):
        self.__name=name
    def get_name(self):
        return self.__name
    name=property(get_name,set_name)

if __name__ == '__main__':
    p1 =person()
    print('Initial EMployee Name-'+p1.name)
    p1.name='John Smith'
    print('After EMployee Name-'+p1.name)