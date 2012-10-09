#!/usr/bin/python
# -*- coding:utf-8 -*-

import random

import matrix

def custom(m, n, elem):
    row = [str(elem)] * n
    raw_matrix = ';'.join([','.join(row)] * m)
    ret = matrix.Matrix(raw_matrix)
    return ret
    
def zeros(m, n):
    return custom(m, n, 0)

def ones(m, n):
    return custom(m, n, 1)

def rand(m, n):
    ret = zeros(m, n)
    for x in xrange(1, m+1):
        for y in xrange(1, n+1):
            ret.set(x, y, random.random())
    return ret
    
def trans(matrix):
    ret = zeros(matrix.n, matrix.m)
    for x in xrange(matrix.n):
        for y in xrange(matrix.m):
            ret.set(x, y, matrix.get(y, x))
    return ret
    
def main():
    A = rand(3,2)
    A.disp('a random matrix A:')
    
    T = trans(A)
    T.disp('transpose of matrix A:')
    
if __name__ == '__main__':
    main()