# Find an Euclidian distance between (2, 3) and (10, 8)
import math


def d(var):
    x1 = var[0][0]
    y1 = var[0][1]
    x2 = var[1][0]
    y2 = var[1][1]
    pre_result = (x2 - x1) ** 2 + (y2 - y1) ** 2
    result = math.sqrt(pre_result)
    return f"The Euclidian Distance between {var[0]} and {var[1]} is √{pre_result} or ~{result}"


print(d([(2, 3), (10, 8)]))
print(d([(3, 4), (7, 1)]))
print(d([(0, 0), (10, 10)]))
print("End of program.")
