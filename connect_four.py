# class Canvas:
#     def __init__(self, width, height):
#         self.width = width
#         self.height = height
#         self.data = [[' '] * width for i in range(height)]
#
#     def setpixel(self, row, col):
#         self.data[row][col] = '*'
#
#     def getpixel(self, row, col):
#         return self.data[row][col]
#
#     def display(self):
#         print("\n".join(["".join(row) for row in self.data]))
#
#
# class Shape:
#     def paint(self, canvas): pass
#
# class Rectangle(Shape):
#     def __init__(self, x, y, w, h):
#         self.x = x
#         self.y = y
#         self.w = w
#         self.h = h
#
#     def hline(self, x, y, w):
#         pass
#
#     def vline(self, x, y, h):
#         pass
#
#     def paint(self, canvas):
#         canvas.setpixel(self.x, self.y)
#         self.hline(self.x, self.y + self.h, self.w)
#         self.vline(self.x, self.y, self.h)
#         self.vline(self.x + self.w, self.y, self.h)
#
# class Square(Rectangle):
#     def __init__(self, x, y, size):
#         Rectangle.__init__(self, x, y, size, size)
#
# class CompoundShape(Shape):
#     def __init__(self, shapes):
#         self.shapes = shapes
#
#     def paint(self, canvas):
#         for s in self.shapes:
#             s.paint(canvas)
# Squreist = Square(10, 5, 20)
#
# print(CompoundShape(Squreist))
#
# c = Canvas(40, 40)
#
# s = Square(2, 2, 3)
#
# print(c.display())
# class Car(object):
#     """A car for sale by Jeffco Car Dealership.
#
#     Attributes:
#         wheels: An integer representing the number of wheels the car has.
#         miles: The integral number of miles driven on the car.
#         make: The make of the car as a string.
#         model: The model of the car as a string.
#         year: The integral year the car was built.
#         sold_on: The date the vehicle was sold.
#     """
#
#     def __init__(self, wheels, miles, make, model, year, sold_on):
#         """Return a new Car object."""
#         self.wheels = wheels
#         self.miles = miles
#         self.make = make
#         self.model = model
#         self.year = year
#         self.sold_on = sold_on
#
#     def sale_price(self):
#         """Return the sale price for this car as a float amount."""
#         if self.sold_on is not None:
#             return 0.0  # Already sold
#         return 5000.0 * self.wheels
#
#     def purchase_price(self):
#         """Return the price for which we would pay to purchase the car."""
#         if self.sold_on is None:
#             return 0.0  # Not yet sold
#         return 8000 - (.10 * self.miles)
#
# my_car = Car('wheel', 10000, 'Toyota', 'camry', 2005, 2008)
#
# print(my_car.purchase_price())
DOT = '.'


class Board(object):
    def __init__(self, cols=7, rows=6):
        self.cols = cols
        self.rows = rows
        self.board = list([[DOT] * rows for void in range(cols)])

    def display(self):
        print(' ', '  '.join(map(str, range(self.cols))))

        for y in range(self.rows):
            print(y, '  '.join(str(self.board[x][y]) for x in range(self.cols)))

    def insert(self, column, coin):
        col = self.board[column]

        if col[0] != DOT:
            raise Exception('Full column, choose another.')

        i = int(self.rows) - 1
        for row in range(self.rows):
            if col[i] == DOT:
                col[i] = coin
                break
            else:
                i -= 1

        self.check_winner()
        self.display()
        print('\n')

    def check_winner(self):
        for row in list(zip(*self.board)):
            count = 0
            temp = row[0]
            for item in row:
                if item == temp:
                    count += 1
                    temp = item
                    if count >= 4 and item != '.':
                        print('Winner is: ', item)
                else:
                    count = 0
                    temp = item
        for col in list(self.board):
            count = 0
            temp = col[0]
            for item in col:
                if item == temp:
                    count += 1
                    temp = item
                    if count >= 4 and item != '.':
                        print('Winner is: ', item)
                else:
                    count = 0
                    temp = item


game = Board(7, 6)
game.insert(3, 'X')
game.insert(3, 'O')
game.insert(2, 'X')
game.insert(2, 'O')
game.insert(1, 'X')
game.insert(4, 'O')
game.insert(5, 'X')
game.insert(2, 'O')
game.insert(3, 'X')
game.insert(3, 'O')
game.insert(1, 'X')
game.insert(1, 'O')
game.insert(0, 'X')
