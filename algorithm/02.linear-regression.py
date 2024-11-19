import math
import numpy as np

x = np.array([1,2,3,4,5])
y = np.array([5,7,9,11,13])

m_curr = b_curr = 0
o = 0
n=len(x)
learning_rate = 0.08

fc = math.inf
count = 0
while fc >= o:
    y_predicted = m_curr * x + b_curr
    md = -(2/n)*sum(x*(y-y_predicted))
    bd = -(2/n)*sum(y-y_predicted)
    m_curr = m_curr - learning_rate * md
    b_curr = b_curr - learning_rate * bd

    fc = (1 / n) * sum(val ** 2 for val in (y - y_predicted))
    count += 1


print(f'after {count} times, find m_curr is {m_curr},b_curr is {b_curr}, final fc is {fc}')



