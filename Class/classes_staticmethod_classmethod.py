class person():
    totalObjects=0
    def __init__(self,name='John Smith'):
        self.name=name
        person.totalObjects+=1
    @classmethod
    def showcount(cls):
        # print(type(person.totalObjects))
        print('In @classmethod total objects----'+str(person.totalObjects))
    @staticmethod
    def greet():
        print('static method greet')
        print('In @staticmethod total objects----'+str(person.totalObjects))
if __name__ == '__main__':
    p1=person()
    p2=person(name='Steve Bruce')

    person.showcount()
    p3 = person(name='Bruce Wayne')
    person.greet()
    del p1.totalObjects
    print(p1.totalObjects)