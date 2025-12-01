# Advent-of-Code-2025

This repository hosts my Python solutions of the Advent of Code 2025 puzzles.
The full puzzle description and the input can be found on [https://adventofcode.com/2025](https://adventofcode.com/2025).
To run the code, the input files need to be placed in the `input` directory.
The files are either named `dayXX.txt` or `dayXX_example.txt` 
where  `XX` has to be replaced with the day as a two-digit numbers.
Further, the one with `_example` in the name, contains the input of the small example given in the puzzle description.
If the second question of the day has a different example, create a `dayXX_example2.txt` file.
Run then day by day with `run.py` 
where in the last lines of the script the day (as integer) and whether the example or "real" input should be used.
`test_all.py` runs, as its name says, all puzzles.
Or at least, all which are solved until that moment.

## Day 1

We have a wheel showing numbers from 0 to 99 and get instructions about how to rotate it.
The instruction says either left or right and for how many steps.
To earn the first start, we needed to count after how many instructions we stop at 0.
My solution is straight forward: Apply the instructions, apply modulo 100 and check if the result is 0.
Then count it (or not).
/
The second start is earned by figuring out, how often we pass 0, no matter if it is at the end of an instruction or not.
First, we need to count if we move 100 or more steps.
If so, we pass 0 guaranteed (since 100 step is one full wheel rotation).
Second, we need to see if we passed once zero, since last time.
We can do this by comparing to the previous location and consider if turned left or right.

## Day 2
