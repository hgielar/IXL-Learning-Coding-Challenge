def function(steps, n):
    """
    The trick here is to realize that the cells with the highest value are those
    that are incremented the most amount of times -- but, since the lower bounds
    start at (0, 0), note that there is at least one cell being incremented at every
    step. This then means that the cell that is incremented every time is the one
    that has the highest value; to find these cells, we take the union across all
    the rows/columns that are incremented at each time, the union will tell us which
    row/column got incremented each time, and thus which is the maximum value.
    """
    row_sets = []
    col_sets = []
    for step in steps:
        row_bound, col_bound = map(int, step.split(' '))
        row_range = list(range(0, row_bound))
        col_range = list(range(0, col_bound))

        row_sets.append(set(row_range))
        col_sets.append(set(col_range))

    row_intersection = set.intersection(*row_sets)
    col_intersection = set.intersection(*col_sets)

    cells = len(row_intersection) * len(col_intersection)

    return cells
