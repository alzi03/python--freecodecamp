class Rectangle:
  def __init__(self, width, height):
    self.height = height
    self.width = width

  def __str__(self):
    return f'Rectangle(width={self.width}, height={self.height})'
    

  def set_width(self, n):
    self.width = n

  def set_height(self, n):
    self.height = n

  def get_area(self):
    return self.width * self.height

  def get_perimeter(self):
    return (2 * self.width) + (2 * self.height)

  def get_diagonal(self):
    return (self.width ** 2 + self.height ** 2) ** 0.5

  def get_picture(self):
    if self.height > 50 or self.width > 50:
      return 'Too big for picture.'
    else:
      output = ''
      for i in range(self.height):
        output += '*' * self.width + '\n'
      return output

  def get_amount_inside(self, shape):
    return self.get_area() // shape.get_area()


class Square(Rectangle):
  def __init__(self, n):
    super().__init__(n, n)
    self.width = n
    self.height = n

  def __str__(self):
    return f'Square(side={self.width})'

  def set_side(self, n):
    self.width = n
    self.height = n

