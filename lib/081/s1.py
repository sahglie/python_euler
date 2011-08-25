#!/opt/local/bin/python

import pdb
import unittest
import sys
import math
from heapq import *


class Graph:
    INF = sys.maxint
    
    def __init__(self, num_nodes):
        self.matrix = []
        for i in range(0, num_nodes):
            self.matrix.append([])
            self.matrix[i].extend([self.INF] * num_nodes)

    def load_data(self, file="matrix.txt"):
        fd = open(file)
        table = [map(int, row.strip().split(",")) for row in fd.readlines()]
        fd.close()
             
        for row in range(0, len(table)):
            for col in range(0, len(table)):
                matrix_col = row * len(table) + col
                if col < len(table)-1:
                    val = table[row][col+1]
                    self.add_edge(matrix_col, matrix_col+1, val)
                if row < len(table)-1:
                    val = table[row+1][col]
                    self.add_edge(matrix_col, len(table) + matrix_col, val)
        
    def add_edge(self, n1, n2, weight):
        self.matrix[n1][n2] = weight

    def adj_nodes(self, node):
        nodes = []
        for i in range(0, len(self.matrix)):
            n = self.matrix[node][i]
            if i != node and n != self.INF:
                nodes.append(i)
        return nodes
    
    def find_shortest_path(self, start, end):
        self.pq = []
        for i in range(1, len(self.matrix)):
            heappush(self.pq, (self.matrix[start][i], i))
            
        curr = start
        while self.pq:
            curr = heappop(self.pq)[1]
            self.__update_shortest_path(start, curr)

    def __update_shortest_path(self, start, curr):
        d = self.matrix[start][curr]
        for node in self.adj_nodes(curr):
            d1 = self.matrix[start][node]
            d2 = self.matrix[curr][node]
            if d1 > d + d2:
                self.matrix[start][node] = d + d2
                self.update_pq(start, node, d + d2)
        heapify(self.pq)
        
    def update_pq(self, start, node, val):
        for i,elem in enumerate(self.pq):
            if elem[1] == node:
                self.pq[i] = (val, node)

if __name__ == "__main__":
    g = Graph(6400)
    g.load_data()
    g.find_shortest_path(0, 6399)
    print 4445 + g.matrix[0][6399]
