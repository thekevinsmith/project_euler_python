# Problem 15 : Statement :  Lattice paths
# Starting in the top left corner of a 2×2 grid, and only being able to move to the right and down,
#  there are exactly 6 routes to the bottom right corner.
# How many such routes are there through a 20×20 grid?
# See the web page

# this is a more difficult algorithmic problem. 6 ways to go down and right.


def num_ways(n):
    # 0x0 = 1 steps = 1 way
    # 1X1 = 2 steps = 2 ways
    # 2x2 = 4 steps = 6 ways
    # 3x3 = 6 steps

def main():
    print()

    # for the 2x2 grid
    N = 6 #'number of paths'
    x1 = ['r', 'd', 'r', 'd']   # 1
    x2 = ['d', 'd', 'r', 'r']   # 2
    x3 = ['r', 'r', 'd', 'd']   # 3
    x4 = ['d', 'r', 'd', 'r']   # 4
    x5 = ['r', 'd', 'd', 'r']   # 5
    x6 = ['d', 'r', 'r', 'd']   # 6

    x1 = ['r', 'r', 'r', 'r', 'r', 'r']
    x2 = ['d', 'd', 'd', 'd', 'd', 'd']
    x2 = ['d', 'd', 'd', 'd', 'd', 'd']

    # for all intensive purposes we could suggest 1 and zero.
    # there is always an equal amount of steps to take.

    #2x2 = 4 X 100 = 400 steps for the 20x20

    # need a total amount of steps, they cant be similar to any other set of steps.

   --  num_ways('20x20') = 10*num_ways('2x2')





if __name__ == '__main__':
    main()