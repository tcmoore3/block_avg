import numpy as np


def block_avg(data, block_size):
    """Break a 2d numpy array into blocks

    Args
    ----
    data : np.ndarray, shape=(m, n)
        The data to block; must be a 2-dimensional array
    block_size : int
        The size of each block

    Returns
    -------
    blocks : np.ndarray, shape=(m/block_size, n)
        The block averaged data
    stds : np.ndarray, shape=(m/block_size, n)
        The standard deviation of each block

    Note that m must not necessarily be divisible by block_size; in the case
    that it isn't, the data is trimmed from the beginning so that it is.
    """
    remainder = data.shape[0] % block_size
    if remainder != 0:
        data = data[remainder:]
    n_blocks = int(data.shape[0] / block_size)
    data = data.reshape((n_blocks, block_size, -1))
    blocks = np.mean(data, axis=1)
    stds = np.std(data, axis=1)
    return blocks, stds
