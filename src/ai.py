import pickle
from random import randint

import chess
from chess.polyglot import open_reader

from board import evaluate_board


class AI:
    depth = 3

    board_caches = {}

    cache_hit = 0
    cache_miss = 0

    try:
        cache = open('data/cache.p', 'rb')
    except IOError:
        cache = open('data/cache.p', 'wb')
        pickle.dump(board_caches, cache)
    else:
        board_caches = pickle.load(cache)

    def __init__(self, board, is_player_white):
        self.board = board
        self.is_ai_white = not is_player_white

        with open_reader('data/opening.bin') as reader:
            self.opening_moves = [
                str(entry.move()) for entry in reader.find_all(board)
            ]

        print(self.opening_moves)

    def ai_move(self):
        global_score = -1e8 if self.is_ai_white else 1e8
        chosen_move = None

        # can move from opening book
        if self.opening_moves:
            chosen_move = chess.Move.from_uci(
                self.opening_moves[randint(0, len(self.opening_moves) // 3)])
        else:
            for move in self.board.legal_moves:
                self.board.push(move)

                local_score = self.minimax(self.depth - 1, self.is_ai_white,
                                           -1e8, 1e8)
                if self.is_ai_white and local_score > global_score:
                    global_score = local_score
                    chosen_move = move
                elif not self.is_ai_white and local_score < global_score:
                    global_score = local_score
                    chosen_move = move

                self.board.pop()

                print(local_score, move)

            print('\ncache_hit: ' + str(self.cache_hit))
            print('cache_hit: ' + str(self.cache_miss))
            print('hit rate: ' + str(self.cache_hit / (
                self.cache_hit + self.cache_miss) * 100) + '%\n')

        print('\n' + str(global_score) + ' ' + str(chosen_move) + '\n')

        self.board.push(chosen_move)

        with open('data/cache.p', 'wb') as cache:
            pickle.dump(self.board_caches, cache)

    def minimax(self, depth, is_maxing_white, alpha, beta):
        if depth == 0:
            self.board_caches[self.hash_board(
                depth, is_maxing_white)] = evaluate_board(self.board)
            return self.board_caches[self.hash_board(depth, is_maxing_white)]

        # if won or lost or drew
        if not self.board.legal_moves:
            self.board_caches[self.hash_board(
                depth, is_maxing_white)] = 1e8 if is_maxing_white else -1e8
            return self.board_caches[self.hash_board(depth, is_maxing_white)]

        # if board in cache
        if self.hash_board(depth, is_maxing_white) in self.board_caches:
            self.cache_hit += 1

            return self.board_caches[self.hash_board(depth, is_maxing_white)]

        # else
        self.cache_miss += 1

        best_score = -1e8 if is_maxing_white else 1e8
        for move in self.board.legal_moves:
            self.board.push(move)

            if is_maxing_white:
                best_score = max(best_score,
                                 self.minimax(depth - 1, False, alpha, beta))
                alpha = max(alpha, best_score)
            else:
                best_score = min(best_score,
                                 self.minimax(depth - 1, True, alpha, beta))
                beta = min(beta, best_score)
            self.board_caches[self.hash_board(depth,
                                              is_maxing_white)] = best_score

            self.board.pop()

            if beta <= alpha:
                break
        self.board_caches[self.hash_board(depth, is_maxing_white)] = best_score
        return self.board_caches[self.hash_board(depth, is_maxing_white)]

    def hash_board(self, depth, is_maxing_white):
        return str(self.board) + ' ' + str(depth) + ' ' + str(is_maxing_white)
