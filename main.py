class chessPiece:
    def __init__(self, pees, pos):
        self.piece = pees
        self.pos = pos

    def __repr__(self):
        pieces = ["pawn", "Bishop", "Knight", "Rook", "Queen", "King"]
        return pieces[self.piece]



class chessBoard:
    def __init__(self):

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

