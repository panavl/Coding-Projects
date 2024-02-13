"""
File: work.py
  Description:

  Student Name: Wei-Yu Chiang
  Student UT EID: wc22968

  Partner Name: Panav Ladha
  Partner UT EID: pl22793

  Course Name: CS 313E
  Unique Number: 52590
  Date Created: 10-04-23
  Date Last Modified: 10-04-23

"""
import sys
import time


def sum_series(lines, k):
    """
    Input: v an integer representing the minimum lines of code and
    k an integer representing the productivity factor
    Output: computes the sum of the series (v + v // k + v // k**2 + ...)
    returns the sum of the series
    """
    total = 0
    while lines > 0:
        total += lines
        lines //= k
    return total

def linear_search(goal, k):
    """
    Input: n an integer representing the total number of lines of code
    k an integer representing the productivity factor
    Output: returns v the minimum lines of code to write using linear search
    """
    lines = 1
    while sum_series(lines, k) < goal:
        lines += 1
    return lines


def binary_search(goal, k):
    """
    Input: n an integer representing the total number of lines of code
    k an integer representing the productivity factor
    Output: returns v the minimum lines of code to write using binary search
    """
    left, right = 1, goal
    while left < right:
        center = (left + right) // 2
        if sum_series(center, k) >= goal:
            right = center
        else:
            left = center + 1
    return left



def main():
    """
    read number of cases
    """
    line = sys.stdin.readline()
    line = line.strip()
    num_cases = int (line)

    for _ in range (num_cases):
        line = sys.stdin.readline()
        line = line.strip()
        inp =  line.split()
        goal = int(inp[0])
        k = int(inp[1])

        start = time.time()
        print("Binary Search: " + str(binary_search(goal, k)))
        finish = time.time()
        print("Time: " + str(finish - start))

        print()

        start = time.time()
        print("Linear Search: " + str(linear_search(goal, k)))
        finish = time.time()
        print("Time: " + str(finish - start))

        print()
        print()

if __name__ == "__main__":
    main()
