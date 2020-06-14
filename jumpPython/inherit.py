class Parent():
    def print_first_name(self):
        print("King Kong")

class Child(Parent):
    def print_last_name(self):
        print("amy")
    #override
    def print_first_name(self):
        print("Monkey")

amy = Child()
amy.print_first_name()
amy.print_last_name()


class amy():
    def print_first_name(self):
        print("amy")

class lex():
    def print_last_name(self):
        print("lex")

#multi inherit
class amylex(amy, lex):
    pass

amylex = amylex()
amylex.print_first_name()
amylex.print_last_name()
