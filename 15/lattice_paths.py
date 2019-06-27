# Problem 15 : Statement :  Lattice paths
# Starting in the top left corner of a 2×2 grid, and only being able to move to the right and down,
#  there are exactly 6 routes to the bottom right corner.
# How many such routes are there through a 20×20 grid?
# See the web page
# this is a more difficult algorithmic problem. 6 ways to go down and right.


# 1   1   1   1
# 1   2   3   4
# 1   3   6   10
# 1   4   10  20

# a = [[1, 2, 3], [4, 5, 6]]
# print(a[0])
# print(a[1])
#
# b = a[0]
# print(b)
# print(a[0][2])
# a[0][1] = 7
# print(a)
# print(b)
# b[2] = 9
# print(a[0])
# print(b)

def main():

    gs = 2
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

    print(grid)

    # again for the heavy stuff
    for x in range(0, gs+1):
        row = []
        for y in range(0, gs+1):
            if y == 0 or x == 0:
                row.append(1)
            else:
                row.append(0)
        grid.append(row)

    # for
    print(grid)

    # array has been initialized.






    # grid = []
    # print(grid)


    # n = 2
    # grid = []
    # for i in range(0, n+1):
    #     for j in range(0, n+1):
    #         paths = grid[i+1, j] + grid[i, j+1]


    # w*h
    # 0x1 grid => paths available = 1
    # 1x1 grid => paths available = 2
    # 2x1 grid => paths available = 3
    # 2x2 grid => paths available = 6
    # 3x1 grid => paths available = 4

    # size = 2 # 2x2
    # grid = [size+1, size+1]
    # print(grid)

    # grid[2, 2] = grid[1, 1] + grid[1, 1]
    # print(grid)



if __name__ == '__main__':
    main()