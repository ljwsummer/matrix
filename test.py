#!/usr/bin/python
# -*- coding:utf-8 -*-

from matrix import  matlib

def test():
    R = matlib.rand(3,3)
    R.disp('A random matrix R:')
    
    T = matlib.trans(R)
    T.disp('Transpose of matrix R:')
    
    I = matlib.eye(3)
    I.disp('A diagonal matrix I:')
    
    matlib.diag(I).disp('Diagonal element of matrix I:')
    matlib.diag([1,2,3]).disp('Make a custom diagonal matrix:')
    
    M = matlib.dot_multi(T, I)
    M.disp('Dot multiply tow matrices:')
    matlib.dot_multi(2, M).disp('Dot multiply a number with a matrix:')

def main():
    test()
    
if __name__ == '__main__':
    main()