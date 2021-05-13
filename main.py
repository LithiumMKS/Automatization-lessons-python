grid = [['.', '.', '.', '.', '.', '.', ],
        ['.', 'O', 'O', '.', '.', '.', ],
        ['O', 'O', 'O', 'O', '.', '.', ],
        ['O', 'O', 'O', 'O', 'O', '.', ],
        ['.', 'O', 'O', 'O', 'O', 'O', ],
        ['O', 'O', 'O', 'O', 'O', '.', ],
        ['O', 'O', 'O', 'O', '.', '.', ],
        ['.', 'O', 'O', '.', '.', '.', ],
        ['.', '.', '.', '.', '.', '.', ]]

'''
for x in grid:
    while grid.index(x) <= int(len(grid) -1):
        xnum = 0
            while y <= int(len(x) - 1):
                print(x[y], end='')
                y += 1
        xnum += 1
'''
for y in range(len(grid[0])-1, -1, -1):
    for x in range(len(grid)):
        print(grid[x][y], end=' ')
    print()
