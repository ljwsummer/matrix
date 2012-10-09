#!/usr/bin/python
# -*- coding:utf-8 -*-


class Matrix:
    
    def __init__(self, raw_matrix):
        self.__parse(raw_matrix)
        self.__check()
    
    def __check(self):
        for x in xrange(self.m):
            assert len(self.matrix[x]) == self.n, 'ERROR invalid raw matrix'
        
    def __parse(self, raw_matrix):
        self.m = -1
        self.n = -1
        
        self.matrix = raw_matrix.split(';')
        self.m = len(self.matrix)
        
        for x in xrange(self.m):
            self.matrix[x] = self.matrix[x].split(',')
            self.matrix[x] = list(map(float, self.matrix[x]))
        self.n = len(self.matrix[0])
    
    def disp(self):
        for x in xrange(self.m):
            for y in xrange(self.n):
                print '%10.3f' % self.matrix[x][y],
            print
        
def test_matrix():
    test = Matrix('1,1;12,3;1000,10')
    print 'row number is %d' % test.m
    print 'col number is %d' % test.n
    test.disp()
            
def main():
    test_matrix()
    

if __name__ == '__main__':
    main()