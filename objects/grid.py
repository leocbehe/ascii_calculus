
class Grid():

   def __init__(self,rows,cols,body=None,xsize=10,ysize=10):
      self.rows = rows
      self.cols = cols
      self.body = body
      self.xsize = float(xsize)
      self.ysize = float(ysize)

   def assign_range_values(self):
      # TODO give options for negative ranges
      xstart = 0
      ystart = 0
      xend = xstart + self.xsize
      yend = ystart + self.ysize
      xinc = self.xsize / self.cols
      yinc = self.ysize / self.rows
      xvals = [x * xinc for x in range(self.cols)]
      yvals = [y * yinc for y in range(self.rows)]

   def populate_grid(self):
      self.body = [[x for x in range(self.cols)] for y in range(self.rows)]
      for row in self.body:
         for col_index in row:
            row[col_index] = "-"
      print(self.body)
