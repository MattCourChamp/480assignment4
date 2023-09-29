# CSI 480 Problem Set 4

In this problem set, you will implement the state maintenance for a MiniMax based Numerical Tic Tac Toe AI. Make sure you have read Chapter 8 of *Classic Computer Science Problems in Python*.

Numerical Tic Tac Toe is a variant of Tic Tac Toe using alternating odd and even numbers:

> The numbers 1 to 9 are used in this game. The first player plays with the odd numbers, the second player plays with the even numbers. All numbers can be used only once. The player who puts down 15 points in a line wins (sum of 3 numbers). ([Wikipedia Article on Tic Tac Toe Variants](https://en.wikipedia.org/wiki/Tic-tac-toe_variants#Numerical_Tic-Tac-Toe))

The code for MiniMax is provided from Chapter 8. You can also use the example of Tic Tac Toe from that chapter as a strong starting point. You will need to implement a special subclass of `Board` that implements the numerical variant. You can play against the AI by running `python3 ntictactoe_ai.py` or run the unit tests as usual in `test_ntictactoe.py`.

## Hints

- Make sure you understand all of the types before you start.
- You don't need to write a lot of code, just the right code.
- When playing the AI, the first computer move may take a few seconds to compute.
- Note that some of the types/names (method signatures for example) have changed from those in the book in order to support numerical tic tac toe needing a more complex type of move object.

## Rules

1. You cannot use any third-party libraries or code.
2. Your solution must use the provided `minimax.py` file.
3. You cannot modify the `minimax.py`, `board.py`, or `test_ntictactoe.py`.
4. You cannot change the unit tests.
5. Cite all of your sources (even if you just look at them) in comments. Cite any people/classmates you discuss the problem with. Cite GitHub Copilot or any AI assistants if they produce snippets of code that are non-trivial. Write something like, “Generated by GitHub Copilot.” 

Violating any of these rules will result in zero credit for the assignment.

## Setup

1. Create your own **private** repository from this repo by hitting the "Use this template" button at the top of the page
2. Add me (@davecom) as a collaborator on your **private** repository.
3. Run the tests by running `python3 -m unittest` or by pushing to GitHub where the tests will automatically run (look for that big beautiful green checkmark).

## Grading

Partial credit will be provided for some tests passing, but not for code written that passes no tests. You are being graded based on working solutions, not amount of code written. Your grade will be the number of tests passed / the total number of tests * 7. For instance, if you pass 3/7 tests, your grade will be 3. Either tests pass or they don't.

## Note on Repository Access

This repository should stay private. If you make it public, you are possibly providing your solution to other students taking the class. Generally the problem sets in this class are not great portfolio projects because they are too small, or contain a significant portion of code that is not your own and therefore do not demonstrate your skill. Please keep your repository private so other students can't use your solution.
