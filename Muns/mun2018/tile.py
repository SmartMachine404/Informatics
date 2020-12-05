#!/usr/bin/python3

M = int(input())

x = int(input())
y = int(input())
w = int(input()) + x % M
h = int(input()) + y % M 

w_tile =  (w + M - 1) // M
h_tile = (h + M - 1) // M 
print(w_tile * h_tile)