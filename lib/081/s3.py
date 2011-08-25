#!/opt/local/bin/python

import pdb
import unittest
import sys
import math
from heapq import *
import itertools



def closest_unvisited(G, start, unvisited):
    adj_vertices = set(G[start].keys()).intersection(unvisited)
    min = adj_vertices.pop()
    for v in adj_vertices:
        if G[start][v] < G[start][min]:
            min = v
    return min


def update_paths(G, start, curr):
    adj_vertices = set(G[curr].keys())

    for v in adj_vertices:
        if G[start][curr] + G[curr][v] < G[start].get(v, sys.maxint):
            G[start][v] = G[start][curr] + G[curr][v]
        

if "__main__" == __name__:
    matrix = []
    with open("matrix.txt") as f:
        for line in f.readlines():
            matrix.append(map(int, line.strip().split(",")))

    G = {}
    num_vertices = len(matrix)**2
    for i in range(0, num_vertices):
        G[i] = {}

    cols = len(matrix)
    rows = len(matrix)
    for row in range(0, rows):
        for col in range(0, cols):
            vertex = row * cols + col
            if col:
                prev_vertex = vertex - 1
                G[prev_vertex][vertex] = matrix[row][col]
            if row:
                prev_vertex = vertex - cols
                G[prev_vertex][vertex] = matrix[row][col]

    unvisited = set(range(1, num_vertices))
    start, curr = 0, 0
    while unvisited:
        curr = closest_unvisited(G, start, unvisited)
        unvisited.remove(curr)
        update_paths(G, start, curr)

    print matrix[0][0] + G[start][6399]
    
