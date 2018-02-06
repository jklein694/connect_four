DOT = '.'
X = 'X'
O = 'O'


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
                        raise Exception('Winner is: ', item)

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
                        raise Exception('Winner is: ', item)

                else:
                    count = 0
                    temp = item


if __name__ == '__main__':

    game = Board(7, 6)
    player = X
    while True:
        game.display()
        column = input('Player {} enter column:'.format(X if player == X else O))
        game.insert(int(column), player)
        player = O if player == X else X
