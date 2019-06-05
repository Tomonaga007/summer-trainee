

def knapsack(capacity, profits, weights):
    """Function to calculate optilmal profit for given items and maximum capacity.
    Uses bottom-up dynamic programming approach.

    Args:
        capacity (int): total capacity of container.
        profits (list): list of profits for all considered items.
        weights (list): list of weights for all considered items.

    Returns:
        tuple: (total profit, list of indecies of taken items).
    """
    # create and solve a grid for all partial solutions
    memo = [[0] * (capacity + 1)]
    for row in range(1, len(profits) + 1):
        memo.append([0] * (capacity + 1))
        item_weight = weights[row - 1]  # get current item weight
        item_value = profits[row - 1]  # get current item profit

        # list comprehentions instead of for loop shorten execution time
        memo[row] = [max(memo[row - 1][col], memo[row - 1][col - item_weight] + item_value)
                     if item_weight <= col else memo[row - 1][col]
                     for col in range(capacity + 1)]

    # backtracks the grid to find total profit and what items have been taken
    row, col = len(profits), capacity
    result = []
    while True:
        if memo[row][col] == 0:
            break
        if memo[row][col] != memo[row - 1][col]:
            result.append(row - 1)
            col -= weights[row - 1]
            row -= 1
        else:
            row -= 1

    return memo[len(profits)][capacity], result


def calculate(usb_size, memes):
    """Function calculates the best set of memes to maximize profit.

    Args:
        usb_size (int): number describing the capacity of the USB stick in GiB.
        memes (list): is a list of 3-element tuples, each with the name, size in MiB, and
        price in caps of a meme.
    Returns:
        tuple: (total value of all memes on the USB stick,
                set of names of taken memes).
    """
    capacity = 1024 * usb_size
    memes = list(set(memes))
    profit = [t[2] for t in memes]
    weights = [t[1] for t in memes]
    total_profit, memes_to_load = knapsack(capacity, profit, weights)
    memes_to_load = {memes[i][0] for i in memes_to_load}
    return (total_profit, memes_to_load)
