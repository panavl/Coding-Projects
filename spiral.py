"""
  File: spiral.py
  Description:

  Student Name: Wei-Yu Chiang
  Student UT EID: wc22968

  Partner Name: Panav Ladha
  Partner UT EID: pl22793

  Course Name: CS 313E
  Unique Number: 52590
  Date Created: 08-28-23
  Date Last Modified: 08-30-23

 Input: n is an odd integer between 1 and 100
 Output: returns a 2-D list representing a spiral
         if n is even add one to n

def create_spiral(n):
    print("REMOVE THIS PRINT AND ADD YOUR CODE")
 Input: spiral is a 2-D list and n is an integer
 Output: returns an integer that is the sum of the
         numbers adjacent to n in the spiral
         if n is outside the range return 0
def sum_adjacent_numbers(spiral, n):
    print("REMOVE THIS PRINT AND ADD YOUR CODE")
"""



def create_spiral(dim):
    """Creates a Spiral given a dimension for the spiral dimeter"""

    # make grid with zeros as placeholders
    spiral = [[0 for j in range(dim)] for i in range(dim)]



    # find center and insert 1
    num = 1
    row = int((dim - 1) / 2)
    col = int((dim - 1) / 2)

    spiral[row][col] = num

    steps = 1

    # right by 1

    while steps < dim:
        col += 1
        num += 1
        spiral[row][col] = num
        for i in range(steps):
            row += 1
            num += 1
            spiral[row][col] = num
        for i in range(steps+1):
            col -= 1
            num += 1
            spiral[row][col] = num
        for i in range(steps+1):
            row -= 1
            num += 1
            spiral[row][col] = num
        for i in range(steps+1):
            col += 1
            num += 1
            spiral[row][col] = num
        steps +=2
    return spiral




def sum_sub_grid(grid, val):
    """
    Input: grid a 2-D list containing a spiral of numbers
           val is a number within the range of numbers in
           the grid
    Output:
    sum_sub_grid returns the sum of the numbers (including val)
    surrounding the parameter val in the grid
    if val is out of bounds, returns 0
    """
    row = 0
    col = 0

    for i, row_val in enumerate(grid):
        if val in row_val:
            row = i
            col = grid[i].index(val)
    total = 0
    for i in range(-1, 2):
        for j in range(-1, 2):
            if i == 0 and j == 0:
                continue
            if 0 <= row + i < len(grid) and 0 <= col + j < len(grid):
                total += grid[row+i][col+j]


    return total





def main():
    """
    A Main Function to read the data from input,
    run the program and print to the standard output.
    """

    # read the dimension of the grid and value from input file
    dim = int(input())

    # test that dimension is odd
    if dim % 2 == 0:
        dim += 1

    # create a 2-D list representing the spiral
    mat = create_spiral(dim)

    while True:
        try:
            sum_val = int(input())

            # find sum of adjacent terms
            adj_sum = sum_sub_grid(mat, sum_val)

            # print the sum
            print(adj_sum)
        except EOFError:
            break


if __name__ == "__main__":
    main()
