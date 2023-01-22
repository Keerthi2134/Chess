class chessPiece:
    def __init__(self, pees, pos):
        self.piece = pees
        self.pos = pos

    def __repr__(self):
        pieces = ["pawn", "Bishop", "Knight", "Rook", "Queen", "King"]
        return pieces[self.piece]



class chessBoard:
    def __init__(self):
        self.board = [[''for i in range(8)] for j in range(8)]

        for a in range(8):
            for b in range(8):
                if a == 1 or a == 6 :
                    self.board[a][b] = chessPiece(0,[a,b])
                elif a == 0 or a == 7 :
                    if b == 0 or b == 7:
                        self.board[a][b] = chessPiece(3, [a, b])
                    elif b == 1 or b == 6:
                        self.board[a][b] = chessPiece(2, [a, b])
                    elif b == 2 or b == 5:
                        self.board[a][b] = chessPiece(1, [a, b])
                    elif b == 3:
                        self.board[a][b] = chessPiece(4, [a, b])
                    elif b == 4:
                        self.board[a][b] = chessPiece(5, [a, b])
        print(self.board)


a = chessBoard()