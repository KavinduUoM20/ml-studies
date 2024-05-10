import numpy as np
import math

def gradient_descent(x,y):
    m_curr = b_curr = 0
    iterations = 10000
    n = len(x)
    learning_rate = 0.01
    for i in range(iterations):
        y_pred = m_curr * x + b_curr
        cost = (1/n) * sum([val**2 for val in (y - y_pred)])
        md = -(2/n) * sum(x * (y-y_pred))
        bd = -(2/n) * sum(y - y_pred)
        m_curr = m_curr - learning_rate * md
        b_curr = b_curr - learning_rate * bd
        print("m {}, b {}, cost {}, iteration {}".format(m_curr, b_curr, cost, i))
        target_value = 1e20
        if math.isclose(cost, target_value):
            break

x = np.array([1,2,3,4,5])
y = np.array([5,7,9,10,11])

gradient_descent(x,y)