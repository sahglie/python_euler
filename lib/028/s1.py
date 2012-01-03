#!/usr/bin/env python


sum, n = 1, 1 
for rows in range(3, 1002, 2):
    for i in range(4):
        n += rows - 1
        sum += n

print sum        

