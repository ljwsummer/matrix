#!/usr/bin/python
# -*- coding:utf-8 -*-

"""
matrix lib
"""

from __future__ import absolute_import

import random
import sys

from matrix import  matrix

__author__ = "Jiawang Liu <ljwsummer@gmail.com>"
__version__ = "1.0.0"

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

# custom diagonal matrix or return the diagonal element of a matrix
def diag(ins):
    if isinstance(ins, matrix.Matrix):
        min = ins.m if ins.m < ins.n else ins.n
        temp = []
        for x in xrange(1, min+1):
            temp.append(str(ins.get(x,x)))
        return matrix.Matrix(';'.join(temp))
    elif isinstance(ins, list):
        ret = zeros(len(ins))
        for x in xrange(1, ret.m+1):
            ret.set(x, x, ins[x-1])
        return ret
    else:
        print >> sys.stderr, 'ERROR the parameter must be a matrix or list.'
        
# transpose of matrix   
def trans(mat):
    ret = zeros(mat.n, mat.m)
    for x in xrange(1, mat.n + 1):
        for y in xrange(1, mat.m + 1):
            ret.set(x, y, mat.get(y, x))
    return ret

# dot multiply two matrices
def _dot_multi_mat(mat1, mat2):
    ret = zeros(mat1.m, mat1.n)
    if mat1.m == mat2.m and mat1.n == mat2.n:
        for x in xrange(1, mat1.m + 1):
            for y in xrange(1, mat1.n + 1):
                ret.set(x, y, mat1.get(x, y) * mat2.get(x, y))
    else:
        print >> sys.stderr, 'ERROR the size of tow matrices are not same.'
        ret = None
    return ret

# dot multiply an element or a matrix with another matrix
def dot_multi(ins, mat):
    ret = None
    if isinstance(ins, int) or isinstance(ins, float):
        ret = custom(mat.m, mat.n, ins)
    if ret != None:
        ret = _dot_multi_mat(ret, mat)
    elif isinstance(ins, matrix.Matrix):
        ret = _dot_multi_mat(ins, mat)
    else:
        print >> sys.stderr, 'ERROR the first parameter must be a matrix or a number.'
        ret = None
    return ret
        
  