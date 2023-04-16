from typing import Tuple, List

import numpy as np

def calculate_hits(m: np.ndarray, iterations: int) -> Tuple[np.ndarray]:
    h = np.ones(shape=(m.shape[1], 1))

    m_t = np.transpose(m)

    for i in range(iterations):
        if i > 0:
            h = np.matmul(m, a)
            mx = np.max(h)
            h /= mx

        if i < iterations - 1:
            a = np.matmul(m_t, h)
            mx = np.max(a)
            a /= mx

    return (h, a)


if __name__ == "__main__":
    matrix = np.array(
        [
            [0, 0, 0, 0, 0, 0, 0],
            [1, 0, 0, 1, 1, 0, 0],
            [0, 0, 0, 0, 1, 0, 0],
            [0, 0, 0, 0, 0, 0, 1],
            [0, 1, 0, 0, 0, 1, 0],
            [0, 0, 0, 0, 0, 0, 0],
            [0, 1, 0, 0, 0, 0, 0]
        ]
    )

    hub, auth = calculate_hits(matrix, 4)

    print(f"authority vector is:\n {hub}")
    print(f"hubs vector is :\n {auth}")


