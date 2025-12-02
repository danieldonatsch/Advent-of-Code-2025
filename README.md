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

Earning the fist star is done by finding numbers in given ranges, which consist of two same substrings.
E.g. is 123123 which consists of 2x 123.
We can find them bey checking the number of digits of the lower end of the range.
Using it's first half of digits and start checking this, and then incrementing it by one, 
until the concatenation of it with itself exceeds the upper bound of the range.
/
The second gold star is earned by finding all numbers which consist of repeated "substrings".
E.g. 121212 consists of 3x 12, 222222 consists of 6x 2, 3x 22 and 2x 222.
Second example is the tricky one, we don't want to count it multiple times, so wee keep track on found numbers.
Besides that, we start with 1, see if n-times 1 is in the range, then increment it by one.
If n-times the pattern exceeds the upper bound of the range, we decrement n by one and keep searching until n < 2.

## Day 2

Wait for tomorrow. :-)

