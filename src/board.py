import chess


class Board:
    def __init__(self):
        self.board = chess.Board()

    def legal_moves(self):
        return self.board.legal_moves

    def push(self, move):
        self.board.push(move)

    def push_san(self, move):
        self.board.push_san(move)

    def pop(self):
        self.board.pop()

    def san(self, move):
        self.board.san(move)

    def print(self):
        print(self.board)

    def evaluate_board(self):
        score = 0

        for square in chess.SQUARES:
            piece = self.board.piece_at(square)

            if piece is not None:
                score += self.piece_value(piece, square)

        return score / 100

    def piece_value(self, piece, square):
        symbol = piece.symbol()
        is_white = not symbol.islower()
        score = 1

        if symbol.lower() == 'p':
            score = 1 * self.pawn_value(square, is_white)
        elif symbol.lower() == 'n':
            score = 3 * self.knight_value(square, is_white)
        elif symbol.lower() == 'b':
            score = 3 * self.bishop_value(square, is_white)
        elif symbol.lower() == 'r':
            score = 5 * self.rook_value(square, is_white)
        elif symbol.lower() == 'q':
            score = 9 * self.queen_value(square, is_white)
        elif symbol.lower() == 'k':
            score = 100 * self.king_value(square, is_white)

        if symbol.islower():
            score *= -1

        return score

    def pawn_value(self, square, is_white):
        white = [ 0, 0, 0, 0, 0, 0, 0, 0, 
                5, 10, 10, -20, -20, 10, 10, 5, 
                5, -5, -10, 0, 0, -10, -5, 5, 
                0, 0, 0, 20, 20, 0, 0, 0, 
                5, 5, 10, 25, 25, 10, 5, 5, 
                10, 10, 20, 30, 30, 20, 10, 10, 
                50, 50, 50, 50, 50, 50, 50, 50, 
                0, 0, 0, 0, 0, 0, 0, 0 ]

        black = [ 0,  0,  0,  0,  0,  0,  0,  0,
                50, 50, 50, 50, 50, 50, 50, 50,
                10, 10, 20, 30, 30, 20, 10, 10,
                5,  5, 10, 25, 25, 10,  5,  5,
                0,  0,  0, 20, 20,  0,  0,  0,
                5, -5,-10,  0,  0,-10, -5,  5,
                5, 10, 10,-20,-20, 10, 10,  5,
                0,  0,  0,  0,  0,  0,  0,  0 ]

        if is_white:
            return white[square]
        else:
            return black[square]

    def knight_value(self, square, is_white):
        white = [ -50,-40,-30,-30,-30,-30,-40,-50, 
                -40,-20,  0,  5,  5,  0,-20,-40,
                -30,  5, 10, 15, 15, 10,  5,-30,
                -30,  0, 15, 20, 20, 15,  0,-30,
                -30,  5, 15, 20, 20, 15,  5,-30,
                -30,  0, 10, 15, 15, 10,  0,-30,
                -40,-20,  0,  0,  0,  0,-20,-40,
                -50,-40,-30,-30,-30,-30,-40,-50 ]

        black = [ -50,-40,-30,-30,-30,-30,-40,-50, 
                -40,-20,  0,  0,  0,  0,-20,-40,
                -30,  0, 10, 15, 15, 10,  0,-30,
                -30,  5, 15, 20, 20, 15,  5,-30,
                -30,  0, 15, 20, 20, 15,  0,-30,
                -30,  5, 10, 15, 15, 10,  5,-30,
                -40,-20,  0,  5,  5,  0,-20,-40,
                -50,-40,-30,-30,-30,-30,-40,-50 ]

        if is_white:
            return white[square]
        else:
            return black[square]

    def bishop_value(self, square, is_white):
        white = [ -20,-10,-10,-10,-10,-10,-10,-20,
                -10,  5,  0,  0,  0,  0,  5,-10,
                -10, 10, 10, 10, 10, 10, 10,-10,
                -10,  0, 10, 10, 10, 10,  0,-10,
                -10,  5,  5, 10, 10,  5,  5,-10,
                -10,  0,  5, 10, 10,  5,  0,-10,
                -10,  0,  0,  0,  0,  0,  0,-10,
                -20,-10,-10,-10,-10,-10,-10,-20 ]

        black = [ -20,-10,-10,-10,-10,-10,-10,-20,
                -10,  0,  0,  0,  0,  0,  0,-10,
                -10,  0,  5, 10, 10,  5,  0,-10,
                -10,  5,  5, 10, 10,  5,  5,-10,
                -10,  0, 10, 10, 10, 10,  0,-10,
                -10, 10, 10, 10, 10, 10, 10,-10,
                -10,  5,  0,  0,  0,  0,  5,-10,
                -20,-10,-10,-10,-10,-10,-10,-20 ]

        if is_white:
            return white[square]
        else:
            return black[square]

    def rook_value(self, square, is_white):
        white = [ 0,  0,  0,  5,  5,  0,  0,  0,
                -5,  0,  0,  0,  0,  0,  0, -5,
                -5,  0,  0,  0,  0,  0,  0, -5,
                -5,  0,  0,  0,  0,  0,  0, -5,
                -5,  0,  0,  0,  0,  0,  0, -5,
                -5,  0,  0,  0,  0,  0,  0, -5,
                5, 10, 10, 10, 10, 10, 10,  5,
                0,  0,  0,  0,  0,  0,  0,  0 ]

        black = [ 0,  0,  0,  0,  0,  0,  0,  0,
                5, 10, 10, 10, 10, 10, 10,  5,
                -5,  0,  0,  0,  0,  0,  0, -5,
                -5,  0,  0,  0,  0,  0,  0, -5,
                -5,  0,  0,  0,  0,  0,  0, -5,
                -5,  0,  0,  0,  0,  0,  0, -5,
                -5,  0,  0,  0,  0,  0,  0, -5,
                0,  0,  0,  5,  5,  0,  0,  0 ]

        if is_white:
            return white[square]
        else:
            return black[square]
    
    def queen_value(self, square, is_white):
        white = [ -20,-10,-10, -5, -5,-10,-10,-20,
                -10,  0,  5,  0,  0,  0,  0,-10,
                -10,  5,  5,  5,  5,  5,  0,-10,
                0,  0,  5,  5,  5,  5,  0, -5,
                -5,  0,  5,  5,  5,  5,  0, -5,
                -10,  0,  5,  5,  5,  5,  0,-10,
                -10,  0,  0,  0,  0,  0,  0,-10,
                -20,-10,-10, -5, -5,-10,-10,-20 ]

        black = [ -20,-10,-10, -5, -5,-10,-10,-20,
                -10,  0,  0,  0,  0,  0,  0,-10,
                -10,  0,  5,  5,  5,  5,  0,-10,
                -5,  0,  5,  5,  5,  5,  0, -5,
                0,  0,  5,  5,  5,  5,  0, -5,
                -10,  5,  5,  5,  5,  5,  0,-10,
                -10,  0,  5,  0,  0,  0,  0,-10,
                -20,-10,-10, -5, -5,-10,-10,-20 ]

        if is_white:
            return white[square]
        else:
            return black[square]

    def king_value(self, square, is_white):
        white = [ 20, 30, 10,  0,  0, 10, 30, 20,
                20, 20,  0,  0,  0,  0, 20, 20,
                -10,-20,-20,-20,-20,-20,-20,-10,
                -20,-30,-30,-40,-40,-30,-30,-20,
                -30,-40,-40,-50,-50,-40,-40,-30,
                -30,-40,-40,-50,-50,-40,-40,-30,
                -30,-40,-40,-50,-50,-40,-40,-30,
                -30,-40,-40,-50,-50,-40,-40,-30 ]

        black = [ -30,-40,-40,-50,-50,-40,-40,-30,
                -30,-40,-40,-50,-50,-40,-40,-30,
                -30,-40,-40,-50,-50,-40,-40,-30,
                -30,-40,-40,-50,-50,-40,-40,-30,
                -20,-30,-30,-40,-40,-30,-30,-20,
                -10,-20,-20,-20,-20,-20,-20,-10,
                20, 20,  0,  0,  0,  0, 20, 20,
                20, 30, 10,  0,  0, 10, 30, 20 ]

        if is_white:
            return white[square]
        else:
            return black[square]
