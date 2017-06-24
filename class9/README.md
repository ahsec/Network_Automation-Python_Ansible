# Class 9 Exercises.

#### * exercise_1.txt *
Create a directory called mytest. In ./mytest create three Python modules
world.py, simple.py, whatever.py.

* These three files should each have a function that prints a statement when
called (func1, func2, func3).
* In each of the three modules use the __name__ technique to separate
executable code from importable code. Each module should contain executable code.
* Verify that you are NOT able to import ./mytest (try this from the directory
that contains ./mytest).
​
#### * exercise_2.txt *
Make mytest a package.
In the __init__.py file import each of the functions in world.py, simple.py and
whatever.py.
Test out your package from the Python interpreter shell.
Make sure you can invoke your three functions using both 'import mytest' and
'from mytest import func1, func2, func3'. Once again do this from the
directory containing ./mytest.

#### * exercise_3.txt *
Add a ```__all__``` variable to your ```__init__.py``` file.

Test out __all__ using ```from mytest import *```
Verify that you can directly execute func1(), func2(), func3().
Once again do this from the directory containing ./mytest.

#### * exercise_4_world.py *
Create a class MyClass in world.py.
This class should require that three variables be passed in upon initialization.
Write two methods associated with this class 'hello' and 'not_hello'.
Have both these methods print a statement that uses all three of the
initialization variables.

#### * exercise_5_world.py *
Write a child class MyChildClass of MyClass. This child class should override
the 'hello' method and print a different statement.

#### * exercise_6_world.py *
Optional bonus question -- have MyChildClass augment the ``` __init__() ```
method.
In other words, the child class should do something additional in the
``` __init__() ``` method yet still call its parent class ``` __init__() ```

#### * exercise_7.txt *
Modify your PYTHONPATH such that the directory containing ./mytest is now on
your PYTHONPATH. Verify this in sys.path.

#### * exercise_8.txt *
Update the ```__init__.py``` file and the ```__all__``` variable to include
MyClass.

#### * exercise_9.py *
Write a Python script in a different directory (not the one containing mytest).

* Verify that you can import mytest and call the three functions func1(),
func2(), and func3().
* Create an object that uses MyClass. Verify that you call the hello() and not_hello() methods.
