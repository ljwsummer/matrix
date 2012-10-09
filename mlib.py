#!/usr/bin/python
# -*- coding:utf-8 -*-

import random

import matrix

# custom matrix
def custom(m, n, elem):
    row = [str(elem)] * n
    raw_matrix = ';'.join([','.join(row)] * m)
    ret = matrix.Matrix(raw_matrix)
    return ret

# zero matrix   
def zeros(m, n = -1):
    if n == -1:
        n = m
    return custom(m, n, 0)

# a matrix whose elements are all 1
def ones(m, n = -1):
    if n == -1:
        n = m
    return custom(m, n, 1)

# random matrix, each element is a random number between 0 and 1
def rand(m, n = -1):
    if n == -1:
        n = m
    ret = zeros(m, n)
    for x in xrange(1, m+1):
        for y in xrange(1, n+1):
            ret.set(x, y, random.random())
    return ret

# diagonal matrix
def eye(m, n = -1):
    if n == -1:
        n = m
    ret = zeros(m, n)
    min = m if m < n else n
    for x in xrange(1, min+1):
        ret.set(x, x, 1)
    return ret

# trnaspose of matrix   
def trans(matrix):
    ret = zeros(matrix.n, matrix.m)
    for x in xrange(matrix.n):
        for y in xrange(matrix.m):
            ret.set(x, y, matrix.get(y, x))
    return ret
    
def test():
    A = rand(3,2)
    A.disp('a random matrix A:')
    
    T = trans(A)
    T.disp('transpose of matrix A:')
    
    I = eye(3)
    I.disp('a diagonal matrix I:')

def main():
    test()
    
if __name__ == '__main__':
    main()