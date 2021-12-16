import numpy as np
import matplotlib.pyplot as plt


def cubic_regression(x, y):
    """
    make a program that performs cubic regression
    """
    # make a matrix
    A = np.array(
        [
            [1, x[0], x[0] ** 2, x[0] ** 3],
            [1, x[1], x[1] ** 2, x[1] ** 3],
            [1, x[2], x[2] ** 2, x[2] ** 3],
            [1, x[3], x[3] ** 2, x[3] ** 3],
        ]
    )
    b = np.array([y[0], y[1], y[2], y[3]])
    # solve the matrix
    c = np.linalg.solve(A, b)
    # make a list of x
    x_list = np.linspace(x[0], x[-1], 100)
    # make a list of y
    y_list = c[0] + c[1] * x_list + c[2] * x_list ** 2 + c[3] * x_list ** 3
    # plot the graph
    plt.plot(x, y, "o", x_list, y_list)
    plt.show()
    return c


if __name__ == "__main__":
    x = np.array([0, 1, 2, 3])
    y = np.array([1, 2, 5, 9])
    c = cubic_regression(x, y)
    print(c)
