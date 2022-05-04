# SudokuSolverWFC
Sudoku Solver using a Wave Function Algorithm.

# How does it work?
The Wave Function Collapse (WFC) algorithm was developed by Maxim Gumin. For a more detailed page about the algorithm, see the [Wikipedia page](https://en.wikipedia.org/wiki/Wave_function_collapse).

### Steps Taken:
1. Select the Sudoku Cube with the lowest entropy (least amount of available states)
2. If the cube already has a value:
    - Found a Solution!
3. If the cube has no value nor available states:
    - Invalid Board! Return to the previous state.
4. Select an state and propagate the selection to the cubes in the same row, column and square

# Examples
Some examples can be found in [tests](https://github.com/andrefpoliveira/SudokuSolverWFC/tree/main/tests). All of them were extracted from [Web Sudoku](https://www.websudoku.com/).

Each test consists of:
- 1 Line with the test number
- 9 lines with 9 numbers each (the board, 0 being empty)
