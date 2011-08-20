#!/opt/local/bin/python

import unittest
import sys
import math


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

    def distance(self, n1, n2):
        return self.matrix[n1][n2]

    def closest_node(self, start, visited):
        closest_unvisited = [0, self.INF]
        for node in range(1, len(self.matrix)):
            node_dist = self.matrix[start][node]
            if (node not in visited) and (node_dist < closest_unvisited[1]):
                closest_unvisited = [node, node_dist]
        return closest_unvisited[0]
    
    def find_shortest_path(self, start, end):
        path = [start]
        visited = set([start])
        curr = start
        while len(visited) < len(self.matrix):
            curr = self.closest_node(start, visited)
            visited.add(curr)
            self.__update_shortest_path(start, curr)

    def __update_shortest_path(self, start, curr):
        d = self.distance(start, curr)
        for node in self.adj_nodes(curr):
            d1 = self.distance(start, node)
            d2 = self.distance(curr, node)
            if d1 > d + d2:
                self.matrix[start][node] = d + d2
            

if __name__ == "__main__":
    g = Graph(6400)
    g.load_data()
    g.find_shortest_path(0, 6399)
    print 4445 + g.matrix[0][6399]
