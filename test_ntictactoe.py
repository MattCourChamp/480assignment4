# ntictactoe_tests.py
# For CSI 480 @ Champlain College
# Copyright 2022 David Kopec
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
import unittest
from minimax import find_best_move
from ntictactoe import NTTTMove, NTTTBoard, NTTTPlayer


class NTTTMinimaxTestCase(unittest.TestCase):
    def test_win1(self):
        won_position: list[int] = [7, 4, 0,
                                   0, 9, 0,
                                   0, 2, 0]
        won_board: NTTTBoard = NTTTBoard(won_position, NTTTPlayer.Odd)
        self.assertTrue(won_board.is_win)

    def test_win2(self):
        won_position: list[int] = [1, 4, 7,
                                   0, 5, 6,
                                   3, 8, 0]
        won_board: NTTTBoard = NTTTBoard(won_position, NTTTPlayer.Even)
        self.assertTrue(won_board.is_win)

    def test_draw(self):
        draw_position: list[int] = [1, 4, 7,
                                    2, 5, 6,
                                    9, 8, 3]
        draw_board: NTTTBoard = NTTTBoard(draw_position, NTTTPlayer.Even)
        self.assertTrue(draw_board.is_draw)

    def test_legal_moves(self):
        test_position: list[int] = [1, 4, 7,
                                   0, 0, 6,
                                   3, 8, 0]
        test_board: NTTTBoard = NTTTBoard(test_position, NTTTPlayer.Odd)
        expected_legal_moves = {NTTTMove(3, 5), NTTTMove(3, 9), NTTTMove(4, 5), NTTTMove(4, 9), NTTTMove(8, 5),
                                NTTTMove(8, 9)}
        self.assertEqual(set(test_board.legal_moves), expected_legal_moves)

    def test_easy_position(self):
        # win in 1 move
        to_win_easy_position: list[int] = [4, 3, 0,
                                           0, 7, 0,
                                           0, 0, 0]
        test_board1: NTTTBoard = NTTTBoard(to_win_easy_position, NTTTPlayer.Even)
        answer1: NTTTMove = find_best_move(test_board1)
        self.assertEqual(answer1, NTTTMove(2, 8))

    def test_block_position(self):
        # must block the win
        to_block_position: list[int] = [4, 5, 8,
                                        0, 7, 9,
                                        0, 0, 0]
        test_board2: NTTTBoard = NTTTBoard(to_block_position, NTTTPlayer.Even)
        answer2: NTTTMove = find_best_move(test_board2)
        self.assertIn(answer2, [NTTTMove(7, 2), NTTTMove(7, 6)])

    def test_hard_position(self):
        # find the best move to win 2 moves
        to_win_hard_position: list[int] = [0, 2, 0,
                                           0, 1, 0,
                                           0, 3, 0]
        test_board3: NTTTBoard = NTTTBoard(to_win_hard_position, NTTTPlayer.Even)
        answer3: NTTTMove = find_best_move(test_board3)
        self.assertIn(answer3, [NTTTMove(6, 8), NTTTMove(8, 8)])


if __name__ == '__main__':
    unittest.main()


