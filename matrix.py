#!/usr/bin/python
# -*- coding:utf-8 -*-


class Matrix:
    
    def __init__(self, raw_matrix):
        self.__parse(raw_matrix)
        self.__check()
    
    # check if the raw input is valid
    def __check(self):
        for x in xrange(self.m):
            assert len(self.matrix[x]) == self.n, 'ERROR invalid raw matrix'
    
    ''' use the same input format of Matlab
        for example, a 2*3 matrix:
          3 2 3
          1 3 4
        its raw expression is: '3,2,3;1,3,4'
        comma to divide the elements in a row
        semicolon to divide the different columns
    '''
    def __parse(self, raw_matrix):
        self.m = -1
        self.n = -1
        
        self.matrix = raw_matrix.split(';')
        self.m = len(self.matrix)
        
        for x in xrange(self.m):
            self.matrix[x] = self.matrix[x].split(',')
            self.matrix[x] = list(map(float, self.matrix[x]))
        self.n = len(self.matrix[0])
    
    # use the same coordinate rule of Matlab
    def get(self, x, y):
        return self.matrix[x-1][y-1]
    
    # use the same coordinate rule of Matlab
    def set(self, x, y, elem):
        self.matrix[x-1][y-1] = elem
    
    # print the whold matrix    
    def disp(self, info = 'Matrix:'):
        print info
        for x in xrange(self.m):
            for y in xrange(self.n):
                print '%10.3f' % self.matrix[x][y],
            print
        
def test_matrix():
    A = Matrix('1,1;12,3;1000,10')
    print 'row number is %d' % A.m
    print 'col number is %d' % A.n
    A.disp('matrix A:')
    A.set(A.m, A.n, 2)
    A.disp('after set the bottom right corner elements as 2, matrix A:')
            
def main():
    test_matrix()

if __name__ == '__main__':
    main()