# ntictactoe_ai.py
# Modified from Classic Computer Science Problems in Python Chapter 8
# Copyright 2018-2022 David Kopec
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
# http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.
from minimax import find_best_move
from ntictactoe import NTTTBoard, NTTTMove, NTTTPlayer

board: NTTTBoard = NTTTBoard()


def get_player_move() -> NTTTMove:
    player_move: NTTTMove = NTTTMove(-1, -1)
    while player_move not in board.legal_moves:
        location: int = int(input("Enter a legal square (0-8):"))
        remaining = (NTTTBoard.EVENS if board.turn == NTTTPlayer.Even else NTTTBoard.ODDS) - set(board.position)
        piece: int = int(input(f"Enter a remaining piece {remaining}:"))
        player_move = NTTTMove(location, piece)
    return player_move


if __name__ == "__main__":
    # main game loop
    while True:
        human_move: NTTTMove = get_player_move()
        board = board.make_move(human_move)
        print(board)
        if board.is_win:
            print("Human wins!")
            break
        elif board.is_draw:
            print("Draw!")
            break
        computer_move: NTTTMove = find_best_move(board)
        print("Computer calculating...")
        print(f"Computer move is {computer_move.piece} on {computer_move.square}")
        board = board.make_move(computer_move)
        print(board)
        if board.is_win:
            print("Computer wins!")
            break
        elif board.is_draw:
            print("Draw!")
            break


