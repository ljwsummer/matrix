#!/usr/bin/python
# -*- coding:utf-8 -*-

from matrix import  matlib

def test():
    A = matlib.rand(3,2)
    A.disp('a random matrix A:')
    
    T = matlib.trans(A)
    T.disp('transpose of matrix A:')
    
    I = matlib.eye(3)
    I.disp('a diagonal matrix I:')
    
    D = matlib.diag(I)
    D.disp('diagonal element of matrix I:')
    
    D = matlib.diag([1,2,3])
    D.disp('a custom diagonal matrix:')

def main():
    test()
    
if __name__ == '__main__':
    main()