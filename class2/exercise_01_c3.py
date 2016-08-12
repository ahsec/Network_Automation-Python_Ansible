#!/usr/bin/env python
"""
Script that imports a function from python script exercise_01_c1.py
located in a random directory
"""
import sys
sys.path.insert(0,"dir_1/dir_2/dir_random")
import exercise_01_c1_d_random

def main():
    exercise_01_c1_d_random.print_hello()

if __name__ == '__main__':
    main()

