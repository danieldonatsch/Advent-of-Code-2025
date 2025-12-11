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
\
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
\
The second gold star is earned by finding all numbers which consist of repeated "substrings".
E.g. 121212 consists of 3x 12, 222222 consists of 6x 2, 3x 22 and 2x 222.
Second example is the tricky one, we don't want to count it multiple times, so wee keep track on found numbers.
Besides that, we start with 1, see if n-times 1 is in the range, then increment it by one.
If n-times the pattern exceeds the upper bound of the range, we decrement n by one and keep searching until n < 2.

## Day 3

We got a series of digits (numbers 0 to 9).
The task was to find the two digits, which form the max.
Re-arranging isn't allowed.
We have two variables for the two digits we keep: `first_digit`, `second_digit`.
Then, we iterate over all available digits except of the last one.
We check, if the current digit is larger than the first one.
If so, we save the current digit in `first_digit` and set `second_digit = -1`.
Otherwise, we check if the current digit increases the second one.
If so, we save the current digit as the `second_digit`.
Otherwise, we move on.
At the end, we compare the last available digit to `second_digit`.
\
Now we wanted to find the twelve digits, which form the largest number.
We do the same as with two, but keep now an array of twelve digits, instead of two variables.
The game stays the same.
The only tricky thing is, how to manage the last twelve digits.
We need to make sure, that we do not use e.g. the third last digit of all available ones as our 8th used digit.
Because then, we would have only two digits left in the available ones but need to fill four blank spots in the used digits.
So, make sure you set the upper bound of the loop correct!

## Day 4

Given is a grid, where each grid cell has either a . or an @.
Cells with an @ can be turned to . if it has max 3 neighbour cells containing an @.
To figure out how many cells can be "flipped" we need to go once through the grid and check every cell.
It the cell has already a . go to the next one.
Otherwise, check all its eight neighbours and count the @.
If four are found, go to the next cell.
If all neighbours are checked and max @ are found, count this sell as "flippable".
\
In the second puzzle we did basically the same with the only difference, that we could go over the grid several times.
So, we actually needed to flip the "flippable" cells and go over the grid again and again, until no more cell could be flipped.

## Day 5

Given where (potentially) overlapping intervals and numbers.
The first gold star was earned by simply checking how many of the numbers where in one of the intervals.
This can be done simply by holding a list of all intervals and then checking each number against each interval until a hit or the end of the interval-list.
It is not the most efficient way of doing it, but sufficient.
\
Second question was, how many numbers in total are covered by the intervals.
To figure this out, we need to make sure, intervals are not overlapping.
Taking the list from part 1 and sorting it by the interval start points is the first step.
Then we go through the first sorted list, check for each interval, if it overlaps with the previous one.
If so, the end point of the previous interval is moved forward to the current interval and the current interval can be dropped.
Then, a second pass through the intervals is needed.
Compute for each interval end point minus starting point plus one to get the number of numbers it covers.
Sum this numbers.

## Day 6

.
\
.


## Day 7

The goal was to follow a beam through a space.
Each time, the beam hits a splitter, it splits and two beams go from there.
To figure out, how often the beam split we can use a BFS:
Check on every "row" of the space where splitters are and check, if they are hit by a beam.
To do so, we keep track with a set, on which positions currently beams are.
\
The second gold star was earned by figuring out, how many possible path exists.
This is done in BFS manner, too.
Now we maintain a dict which keeps track of the current beam location and counts the possible path to that location.
We again go row by row through the space.
But this time we check all beam locations.
If a beam location hits a splitter, the beam stops at this location, but it continues on both of its neighbours.
Update the dict accordingly, but make sure to not over-write existing values.

## Day 8

We have some three-dimensional points, and we look for the closest connections between them.
We compute this and save them in a list.
It's an O(n^2) operation, but probably nothing faster is possible.
Then we sort it (O(n log(n))) according to the distance.
Now we can build the circuits in a greedy manner:
We connect the closest two nodes, then we check to which two existing circuits these two nodes belong.
This is a search through all circuits.
If the circuits are stored in a list of sets, it's an operation linear in the length of the list.
We unify the two sets.
\
The first gold star is earned by connecting the 1000 closest distances.
So, we do the above described process 1000 times.
\
The second gold star is earned by finding the connection which finally puts all nodes into one circle.
So, we repeat the process, until the list of circuits has length one.


## Day 9

.
\
.


## Day 10

The first gold star can be earned by implementing breath first search with some optimisation.
In my case, I converted the state of the indicator lights as well as the buttons as binary strings.
These I convert into integers, which reduces the memory usage.
Further, the update can be done with an XOR.
To make sure, the same state isn't checked several times, the list of light states is a set.
\
.


## Day 11

Both gold stars could be earned by finding and counting path through a graph.
In both cases, a depth first search (dfs) method leaded to the correct result.
Since the graph can be quite large, it is very helpful to use caching and make sure, no node is visited more than once.
\
For the second gold star, there was an additional constraint to the path.
Only paths, which pass through specific nodes counted.
So, we need to track this with two boolean variables which we pass through the dfs.

## Day 12

.
\
.

