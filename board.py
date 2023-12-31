# board.py
# Modified From Classic Computer Science Problems in Python Chapter 8
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
from __future__ import annotations
from typing import TypeVar, Generic
from abc import ABC, abstractmethod

Move = TypeVar('Move')


class Player:
    @property
    def opposite(self) -> Player:
        raise NotImplementedError("Should be implemented by subclasses.")


class Board(ABC, Generic[Move]):
    @property
    @abstractmethod
    def turn(self) -> Player:
        ...

    @abstractmethod
    def make_move(self, move: Move) -> Board:
        ...

    @property
    @abstractmethod
    def legal_moves(self) -> list[Move]:
        ...

    @property
    @abstractmethod
    def is_win(self) -> bool:
        ...

    @property
    def is_draw(self) -> bool:
        return (not self.is_win) and (len(self.legal_moves) == 0)

    @abstractmethod
    def evaluate(self, player: Player) -> float:
        ...

