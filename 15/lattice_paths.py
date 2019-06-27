# Problem 15 : Statement :  Lattice paths
# Starting in the top left corner of a 2×2 grid, and only being able to move to the right and down,
#  there are exactly 6 routes to the bottom right corner.
# How many such routes are there through a 20×20 grid?
# See the web page
# this is a more difficult algorithmic problem. 6 ways to go down and right.


def main():

    gs = 20
    grid = []

    # this sets up the basics
    for x in range(0, gs+1):
        row = []
        for y in range(0, gs+1):
            if y == 0 or x == 0:
                row.append(1)
            else:
                row.append(0)
        grid.append(row)

    # print(grid)

    # apply the heavy lifting.
    for i in range(1, gs+1):
        for j in range(1, gs+1):
            grid[i][j] = grid[i-1][j] + grid[i][j-1]
    # print(grid)
    print(grid[gs][gs])

if __name__ == '__main__':
    main()