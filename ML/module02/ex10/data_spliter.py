import numpy as np

def data_spliter(x, y, proportion):
    indexes = np.arange(y.shape[0])
    np.random.shuffle(indexes)
    return(np.split(x[indexes], [int(x.shape[0] * proportion)]), np.split(y[indexes], [int(y.shape[0] * proportion)]))

if __name__ == '__main__':
    x1 = np.array([1, 42, 300, 10, 59])
    y = np.array([0,1,0,1,0])
    # Example 0:
    #print(data_spliter(x1, y, 0.8))
    X, Y = data_spliter(x1, y, 0.8)
    print(X[0], Y[0])
    print(X[1], Y[1])
    # Example 1:
    print(data_spliter(x1, y, 0.5))
    x2 = np.array([[ 1, 42],
    [300, 10],
    [ 59, 1],
    [300, 59],
    [ 10, 42]])
    y = np.array([0,1,0,1,0])
    # Example 2:
    print(data_spliter(x2, y, 0.8))
    # Example 3:
    print(data_spliter(x2, y, 0.5))