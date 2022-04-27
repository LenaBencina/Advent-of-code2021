with open('Input/input4.txt') as f:
    input_random_numbers = f.read().split('\n\n')
    random_numbers_string = input_random_numbers.pop(0)
    random_numbers = [int(x) for x in random_numbers_string.split(',')]

# parse boards to list of lists
board_grids_tmp = list(map(lambda x: x.strip().split('\n'), input_random_numbers))
board_grids = [[list(map(int, x.strip().replace('  ', ' ').split(' '))) for x in i] for i in board_grids_tmp]


# define class
class Board:
    def __init__(self, grid, size, id):
        self.id = id
        self.grid = grid
        self.size = size
        self.marked_grid = [[None for j in range(size)] for i in range(size)]
        self.win = None

    def mark_number(self, new_number):
        for row_index in range(self.size):
            for column_index in range(self.size):
                if self.grid[row_index][column_index] == new_number:
                    self.marked_grid[row_index][column_index] = new_number
        #return self

    def check_if_complete(self):
        # check row
        is_complete_row = any([sum([not i for i in row]) == 0 for row in self.marked_grid])
        # check column (transpose the grid first)
        marked_grid_transposed = list(map(list, zip(*self.marked_grid)))
        is_complete_column = any([sum([not isinstance(i, int) for i in column]) == 0 for column in marked_grid_transposed])
        if counter_wins == len(board_grids) - 1:
            print
        return is_complete_row or is_complete_column

    def get_sum_unmarked(self):
        sum_unmarked = 0
        for row_index in range(self.size):
            for column_index in range(self.size):
                if not self.marked_grid[row_index][column_index]:
                    sum_unmarked += self.grid[row_index][column_index]
        return sum_unmarked

    def set_place(self):
        self.win = True


counter_wins = 0


def get_score():
    global counter_wins
    size = 5
    boards = [Board(grid, size, id) for id, grid in enumerate(board_grids)]  # define boards
    for number in random_numbers:
        for board in boards:
            board.mark_number(number)
            if board.check_if_complete():
                if not board.win:
                    board.set_place()
                    counter_wins += 1
                if counter_wins == 1:
                    sum_unmarked = board.get_sum_unmarked()
                    print('score 1:' + str(sum_unmarked * number))
                if counter_wins == len(boards):
                    sum_unmarked = board.get_sum_unmarked()
                    return sum_unmarked * number


print(get_score())
