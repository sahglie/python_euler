#!/opt/local/bin/python

import sys

class Graph:
    def __init__(self, file_name="matrix.txt"):
        self.grid = self.__load_grid(file_name)
        self.num_vertices = len(self.grid)**2        
        self.G = self.__init_G(self.grid, self.num_vertices)

    def calc_shortest_path(self, start, end):
        unvisited = set(range(0, self.num_vertices))
        curr = unvisited.remove(start)
        while unvisited:
            curr = self.__closest_unvisited(start, unvisited)
            self.__update_paths(start, curr)

        return self.grid[start][start] + self.G[start][end]

    def __init_G(self, grid, num_vertices):
        G = {}
        for i in range(0, num_vertices):
            G[i] = {}

        cols, rows = len(grid), len(grid)
        for row in range(0, rows):
            for col in range(0, cols):
                vertex = row * cols + col
                if col:
                    prev_vertex = vertex - 1
                    G[prev_vertex][vertex] = grid[row][col]
                if row:
                    prev_vertex = vertex - cols
                    G[prev_vertex][vertex] = grid[row][col]
        return G
    
    def __closest_unvisited(self, start, unvisited):
        adj_vertices = set(self.G[start].keys()).intersection(unvisited)
        min = adj_vertices.pop()
        for v in adj_vertices:
            if self.G[start][v] < self.G[start][min]:
                min = v
        unvisited.remove(min)
        return min

    def __update_paths(self, start, curr):
        adj_vertices = set(self.G[curr].keys())
        for v in adj_vertices:
            if self.G[start][curr] + self.G[curr][v] < self.G[start].get(v, sys.maxint):
                self.G[start][v] = self.G[start][curr] + self.G[curr][v]

    def __load_grid(self, file_name):
        grid = []
        with open(file_name) as f:
            for line in f.readlines():
                grid.append(map(int, line.strip().split(",")))
        return grid


if "__main__" == __name__:
    g = Graph("matrix.txt")
    print g.calc_shortest_path(0, 6399)
    
