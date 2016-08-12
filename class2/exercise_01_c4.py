#!/usr/bin/env python
"""
Script that imports a function from python script exercise_01_c1.py
located in the ~/applied_python/lib/python2.7/site-packages/ directory
"""
import sys
sys.path.insert(0,"~/applied_python/lib/python2.7/site-packages/")
import exercise_01_c1_d_lib

def main():
    exercise_01_c1_d_lib.print_hello()

if __name__ == '__main__':
    main()

