# ntictactoe.py
# For CSI 480 @ Champlain College
# Starter Code by David Kopec
# Completed by:
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

    def __repr__(self) -> str:
        nice_version = [str(p) if p != 0 else " " for p in self.position]
        return f"""{nice_version[0]}|{nice_version[1]}|{nice_version[2]}
-----
{nice_version[3]}|{nice_version[4]}|{nice_version[5]}
-----
{nice_version[6]}|{nice_version[7]}|{nice_version[8]}"""
