# Grid Game

Julia is playing a game on an infinite two-dimensional grid, where the bottom left cell is referenced as (1,1) and each cell contains an initial value of 0. The game consists of *n* steps; during each step:

1. Julia has two integers *r* and *c*.
2. Julia increments the value in every *(i, j)* cell satisfying 1 <= i <= r and 1 <= j <= c by 1.

After performing *n* such steps, Julia finds the maximum value, *x*, in any cell on the board, and counts the number of occurrences of *x*.

Complete the function in the editor below. It has the following parameter:

| Name | Type | Description |
| ---- | ---- | ----------- |
| steps | string array | Each index contains a string of two-space separated integers describing the respective values of *r* and *c* for each step. |

The function must return a long integer denoting the total number of ocurrences of the greatest integer *x* in the grid after *n* steps.

# Input format 
The first line contains an integer, *n*, denoting the number of elements in steps. Each of the subsequent lines contains a string of two space-separated integers describing an index in steps.

# Constraints

* 1 <= n <= 100
* 1 <= r, c <= 10^6

# Output format 

Return a long integer denoting the total number of occurrences of the greatest integer *x* in the grid after *n* steps.
