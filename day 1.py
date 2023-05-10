# Find an Euclidian distance between (2, 3) and (10, 8)


# Calculate the Square root
def sqr(x):
    a = 1
    compe = 0
    while a < 1000:
        compe = a * a
        if x - compe == 0:
            return a
        else:
            a += 1
    return f"Cannot find the square root of {x} "

def distance(p,q):
    calc = (p-q) ** 2
    return sqr(calc)

print(distance(2,3))
print(distance(10,8))

print(sqr(89))