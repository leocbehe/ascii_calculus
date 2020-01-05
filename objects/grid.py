
class Grid():

   def __init__(self,rows,cols,body=None,xsize=10,ysize=10):
      self.rows = rows
      self.cols = cols
      self.body = body
      self.xsize = float(xsize)
      self.ysize = float(ysize)
      self.xvals = 0
      self.yvals = 0

   def assign_range_values(self):
      # TODO give options for negative ranges
      xstart = 0
      ystart = 0
      self.xinc = self.xsize / self.cols
      self.yinc = self.ysize / self.rows
      # The yvals list is reversed in its range direction just because of the
      # default order that for loops would print stuff out. It's just flipped so
      # it looks right in the printout.
      self.xvals = [x * self.xinc for x in range(xstart, xstart + self.cols)]
      self.yvals = [y * self.yinc for y in range(ystart + self.rows-1, ystart-1, -1)]
      print(len(self.yvals))

   def populate_grid(self, func):
      self.body = [[x for x in range(self.cols)] for y in range(self.rows)]
      func_values = [func(x) for x in self.xvals]
      row_index = 0
      for row in self.body:
         for col_index in row:
            if self.func_match(row_index, col_index, func_values):
               row[col_index] = "X"
            else:
               row[col_index] = "- "
         row_index += 1

   def func_match(self, row_index, col_index, func_values):
      current_func_value = func_values[col_index]
      current_y_value = self.yvals[row_index]
      upper_bound = current_y_value + self.yinc / 2
      lower_bound = current_y_value - self.yinc / 2
      return ( current_func_value < upper_bound and current_func_value >
lower_bound)

   def display(self):
      for row in self.body:
         for col in row:
            print("{:3}".format(col), end='')
         print()
