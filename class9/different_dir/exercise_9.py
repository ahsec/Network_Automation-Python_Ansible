#!/usr/bin/env python
'''
9. Write a Python script in a different directory (not the one containing
mytest).

 a. Verify that you can import mytest and call the three functions func1(),
 func2(), and func3().
 b. Create an object that uses MyClass. Verify that you call the hello() and
 not_hello() methods.
'''
from mytest import *

def main():
    print '[+] Calling func1: '
    func1()
    print '[+] Calling func2: '
    func2()
    print '[+] Calling func3: '
    func3()

    print '+'*40
    print '[+] Creating a new object from class MyClass'
    a_class = MyClass('var_a', 'var_b', 'var_c')
    print '[+] Calling function hello from MyClass:'
    a_class.hello()
    print '[+] Calling function not_hello from MyClass:'
    a_class.not_hello()

if __name__ == '__main__':
    main()
