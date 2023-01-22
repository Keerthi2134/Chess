from termcolor import colored

class chessPiece:
    def __init__(self, pees, pos):
        self.piece = pees
        self.pos = pos

    def __repr__(self):
        pieces = ["pawn", "Bishop", "Knight", "Rook", "Queen", "King"]
        return pieces[self.piece]



class chessBoard:
    def __init__(self):
        self.chessBoard = self.initialize()
    
    def initialize(self):
        chessBoard = [["X" for i in range(8)] for j in range(8)]

        for i in range(8):
            board[1][i] = "P"
            board[6][i] = "P"

        for i in range(0, 8, 7):
            board[i][0] = "R"
            board[i][1] = "G"
            board[i][2] = "B"
            board[i][3] = "Q"
            board[i][4] = "K"
            board[i][5] = "B"
            board[i][6] = "G"
            board[i][7] = "R"
        return board

    def print_board(self):
        numbers = '87654321'
        print()
        for i in range(8):
            print(numbers[i], end="  ")
            for k in range(8):
                print(self.board[i][k], end=" ")
            print()
        print("   A B C D E F G H")

    @staticmethod
    def convert_letter_to_num(posn):
        """Convert a posn.x value from letter to number for indexing in the board array"""
        letters = 'ABCDEFGH'
        i = 0
        for letter in letters:
            if posn.x == letter:
                return i
            i += 1

    def update_board(self, from_posn, piece):
        old_x_value = self.convert_letter_to_num(from_posn)
        new_x_value = self.convert_letter_to_num(piece.posn)

        # Must take 8 less the old y value
        # Note: the board's x, y values are switched compared to Piece x, y values >.<
        is_capture, value = self.capture_piece(piece, new_x_value)
        if is_capture:
            print(colored("Your {0} captured the Bot's {1}!", "green").format(piece.type, self.convert_value_to_type(value)))
        self.board[8 - int(from_posn.y)][old_x_value] = "X"
        self.board[8 - int(piece.posn.y)][new_x_value] = piece.shape

    def capture_piece(self, piece, x_posn):
        value = self.board[8 - int(piece.posn.y)][x_posn]
        if value != "X":
            return True, value
        return False, value

    @staticmethod
    def convert_value_to_type(value):
        if value == "P":
            return "Pawn"
        if value == "R":
            return "Rook"
        if value == "G":
            return "Knight"
        if value == "B":
            return "Bishop"
        if value == "Q":
            return "Queen"
        if value == "K":
            return "King"
        

'''
        alphanumboard = {}
        for indi , i in enumerate(list("12345678")):
            for indj, j in enumerate(list("abcdefgh")):
                alphanumboard[j+i] = [indi,indj]
        actualboard = [(['']*8)]*8

        for a in range(8):
            for b in range(8):
                if a == 1 or a == 6:
                    actualboard[a][b] = chessPiece(0, [a, b])
                elif (b == 0 or b == 7) and (a == 0 or a == 7):
                    actualboard[a][b] = chessPiece(3, [a, b])
                elif (b == 1 or b == 6) and (a == 0 or a == 7):
                    actualboard[a][b] = chessPiece(2, [a, b])
                elif (b == 2 or b == 5) and (a == 0 or a == 7):
                    actualboard[a][b] = chessPiece(1, [a, b])
                elif (b == 3) and (a == 0 or a == 7):
                    actualboard[a][b] = chessPiece(4, [a, b])
                elif (b == 4) and (a == 0 or a == 7):
                    actualboard[a][b] = chessPiece(5, [a, b])
        print(actualboard)

a = chessBoard()
'''
