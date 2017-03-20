class Parent():

    def print_last_name(self):
        print('Robert')

class Child(Parent):

    def print_first_name(self):
        print('Tom')

    def print_last_name(self):
        print('Tuna')

tom = Child()
tom.print_first_name()
tom.print_last_name()