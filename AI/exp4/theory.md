Experiment 4
Title

Implementation of N-Queens Problem using Backtracking and Branch & Bound Technique in Java

Based on your uploaded Practical 4 file

Aim

To implement the N-Queens problem using:

Backtracking,
and Branch & Bound techniques in Java.
Objectives
To understand constraint satisfaction problems.
To solve N-Queens problem using Backtracking.
To optimize solution using Branch and Bound technique.
Theory
Introduction to N-Queens Problem

N-Queens problem is a classical Artificial Intelligence problem.

Goal:
Place N queens on an N × N chessboard such that:

no two queens attack each other.

Queens attack:

horizontally,
vertically,
diagonally.

For:

N = 4

we must place 4 queens safely.

Constraints

No two queens should be in:

same row,
same column,
same diagonal.
Backtracking Technique

Backtracking is a recursive problem-solving technique.

Working:

Place queen safely.
Move to next row.
If conflict occurs:
remove queen,
backtrack,
try another position.

Backtracking explores all possible solutions systematically.

Branch and Bound Technique

Branch and Bound improves Backtracking by:

reducing unnecessary searches,
using additional arrays for constraints.

It checks:

occupied columns,
left diagonals,
right diagonals

before placing queens.

This improves efficiency.

Applications
Chess problems
Scheduling
Constraint satisfaction problems
Resource allocation
AI search problems
Algorithm
Backtracking Algorithm
1. Start from first row.
2. Try placing queen in each column.
3. Check safety conditions.
4. If safe:
      place queen.
5. Recursively solve next row.
6. If no solution:
      backtrack.
7. Repeat until all queens placed.
Branch and Bound Algorithm
1. Use arrays to track occupied positions.
2. Check column and diagonals quickly.
3. Place queen safely.
4. Move recursively to next row.
5. Backtrack if conflict occurs.