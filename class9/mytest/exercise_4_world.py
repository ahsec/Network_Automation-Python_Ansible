#!/usr/bin/env python

def func3():
    print "From world.py"

class MyClass(object):
    def __init__(self, var_a, var_b, var_c):
        self.var_a = var_a
        self.var_b = var_b
        self.var_c = var_c
    def hello(self):
        print 'Method-Hello from MyClass. Vars are: {} {} {}'.format(self.var_a,
                                                                     self.var_b,
                                                                     self.var_c)
    def not_hello(self):
        print 'Method-Not Hello from MyClass. Vars are: {} {} {}'.format(self.var_a,
                                                                         self.var_b,
                                                                         self.var_c)
def main():
    pass

if __name__ == '__main__':
    main()
