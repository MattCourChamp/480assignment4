# ntictactoe.py
# For CSI 480 @ Champlain College
# Starter Code by David Kopec
# Completed by: Matthew Cournoyer
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
from __future__ import annotations
from enum import Enum
from board import Player, Board, Move
from typing import NamedTuple


class NTTTPlayer(Player, Enum):
    Even = "Even"
    Odd = "Odd"

    @property
    def opposite(self) -> NTTTPlayer:
        if self == NTTTPlayer.Even:
            return NTTTPlayer.Odd
        else:
            return NTTTPlayer.Even

    def __str__(self) -> str:
        return self.value


class NTTTMove(NamedTuple):
    square: int
    piece: int


class NTTTBoard(Board[NTTTMove]):
    EVENS = set([2, 4, 6, 8])
    ODDS = set([1, 3, 5, 7, 9])

    def __init__(self, position: list[int] = [0, 0, 0, 0, 0, 0, 0, 0, 0], turn: NTTTPlayer = NTTTPlayer.Odd) -> None:
        self.position: list[int] = position
        self._turn: NTTTPlayer = turn

    # Implement your versions of the methods in the Board class here
    # Remember, you saw the analogous TTTBoard in Chapter 8 of CCSPiP
    # Think about what changes in numerical and what you have been provided
    # Note that several of the related types have changed from the TTTBoard
    # YOUR CODE HERE

    @property
    def turn(self) -> NTTTPlayer:
        """Returns the current player"""
        return self._turn

    def make_move(self, move: NTTTMove) -> NTTTBoard:
        """Returns a copy of the board with the new move"""
        temp_position = self.position.copy()
        temp_position[move.square] = move.piece
        return NTTTBoard(temp_position, self.turn.opposite)

    @property
    def legal_moves(self) -> list[NTTTMove]:
        """Returns a list of possible moves"""
        played_nums = set(self.position)
        if self._turn == NTTTPlayer.Even:
            return [NTTTMove(s, p) for s in range(len(self.position)) for p in self.EVENS if self.position[s] == 0 and not played_nums.__contains__(p)]
        else:
            return [NTTTMove(s, p) for s in range(len(self.position)) for p in self.ODDS if self.position[s] == 0 and not played_nums.__contains__(p)]


    @property
    def is_win(self) -> bool:
        """Is there a 15 in any row, column, or diagonal, also makes sure there are no zeroes in a winning trio"""
        return (self.position[0] + self.position[1] + self.position[2] == 15 and (self.position[0] != 0 and self.position[1] != 0 and self.position[2] != 0)) or \
               (self.position[3] + self.position[4] + self.position[5] == 15 and (self.position[3] != 0 and self.position[4] != 0 and self.position[5] != 0)) or \
               (self.position[6] + self.position[7] + self.position[8] == 15 and (self.position[6] != 0 and self.position[7] != 0 and self.position[8] != 0)) or \
               (self.position[0] + self.position[3] + self.position[6] == 15 and (self.position[0] != 0 and self.position[3] != 0 and self.position[6] != 0)) or \
               (self.position[1] + self.position[4] + self.position[7] == 15 and (self.position[1] != 0 and self.position[4] != 0 and self.position[7] != 0)) or \
               (self.position[2] + self.position[5] + self.position[8] == 15 and (self.position[2] != 0 and self.position[5] != 0 and self.position[8] != 0)) or \
               (self.position[0] + self.position[4] + self.position[8] == 15 and (self.position[0] != 0 and self.position[4] != 0 and self.position[8] != 0)) or \
               (self.position[2] + self.position[4] + self.position[6] == 15 and (self.position[2] != 0 and self.position[4] != 0 and self.position[6] != 0))

    @property
    def is_draw(self) -> bool:
        return (not self.is_win) and (len(self.legal_moves) == 0)

    def evaluate(self, player: NTTTPlayer) -> float:
        """Checks if the board wins, loses, or ties. Is only ran when the board is full or someone wins."""
        if self.is_win and self._turn == player:
            return -1
        elif self.is_win and self._turn != player:
            return 1
        else:
            return 0

    def __repr__(self) -> str:
        nice_version = [str(p) if p != 0 else " " for p in self.position]
        return f"""{nice_version[0]}|{nice_version[1]}|{nice_version[2]}
-----
{nice_version[3]}|{nice_version[4]}|{nice_version[5]}
-----
{nice_version[6]}|{nice_version[7]}|{nice_version[8]}"""
