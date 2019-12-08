import os
import sys
import objects.grid

def main():
   grid = objects.grid.Grid(30, 50)
   grid.assign_range_values()
   grid.populate_grid()

if __name__ == "__main__":
   main() 
