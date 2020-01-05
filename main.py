import os
import sys
import objects.grid

def main():
   grid = objects.grid.Grid(60, 80)
   grid.assign_range_values()
   grid.populate_grid(graph_function)
   grid.display()

def graph_function(x):
   return x**(1.7)

if __name__ == "__main__":
   main() 
