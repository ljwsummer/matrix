#!/usr/bin/python
# -*- coding:utf-8 -*-

from matrix import  mlib

def test():
    A = mlib.rand(3,2)
    A.disp('a random matrix A:')
    
    T = mlib.trans(A)
    T.disp('transpose of matrix A:')
    
    I = mlib.eye(3)
    I.disp('a diagonal matrix I:')
    
    D = mlib.diag(I)
    D.disp('diagonal element of matrix I:')
    
    D = mlib.diag([1,2,3])
    D.disp('a custom diagonal matrix:')

def main():
    test()
    
if __name__ == '__main__':
    main()