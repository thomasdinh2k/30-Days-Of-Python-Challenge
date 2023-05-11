import math, time

age = 23
height = 17.8
complex = 1 + 1j


def triangle_area():
    h = int(input("height? "))
    b = int(input("base? "))
    return int(0.5 * h * b)


def rectangle_area():
    l = int(input("length? "))
    w = int(input("width? "))
    area = l * w
    perimeter = 2 * (l + w)
    print(f"Area: {area} and Perimeter: {perimeter}")


def circle_radius():
    r = int(input("Radius of Circle = "))
    area = math.pi * r * r
    circumference = 2 * math.pi * r
    print(f"Area: {area} and Circumference: {circumference}")


# Exercise 8
def calc_slope(equation):
    print(f'Calculating slope using equation: {equation}')
    terms = equation.split()
    slope = float(terms[2][:-1])
    b = float(terms[-1])
    print(f'We have slope = {slope} and b = {b}')
    print('x = (-b)/m')
    print(f'Which means x = (-{b}/{slope})')
    x = -b / slope
    print('Calculation Complete!')
    print(f'Slope = {slope}\nX-intercept = {x}\nY-intercept = {b}')
    print('\n')
    return slope


# Exercise 9

def calc_slope_and_Euclidean_distance(two_point_lst, equation):
    x1 = two_point_lst[0][0]
    x2 = two_point_lst[1][0]
    y1 = two_point_lst[0][1]
    y2 = two_point_lst[1][1]
    print(f'Calculating slope using equation: {equation}')
    terms = equation.split()
    equation = equation.format(y2=y2, y1=y1, x2=x2, x1=x1)
    eq_terms = terms[-1:][0]
    m = eval(eq_terms)
    print(f'Slope= {m}')

    pre_result = (x2 - x1) ** 2 + (y2 - y1) ** 2
    result = math.sqrt(pre_result)
    print(f'Euclidean distance= {result}')
    return m


# Exercise 10
ex8 = calc_slope("y = 2x - 2")
ex9 = calc_slope_and_Euclidean_distance([(2, 2), (6, 10)], 'm = (y2-y1)/(x2-x1)')

if ex8 < ex9:
    print('ex8 < ex9')
elif ex8 == ex9:
    print('ex8 = ex9')
else:
    print('ex8 < ex9')


# Exercise 11
def find_x():
    x = 0
    y = x ** 2 + 6 * x + 9
    while y != 0:
        print(f'Trying x = {x}')
        y = x ** 2 + 6 * x + 9
        print(f"y = {y}")
        x -= 1
        time.sleep(.5)
    print(f"Found that if x = {x + 1} than y = 0")


# Exercise 12
falsey = len('dragon') != len('python')
print(falsey)

# Exercise 13
print('on' in 'python' and 'on' in 'dragon')

# Exercise 14
print('jargon' in 'I hope this course is not full of jargon')

# Exercise 15
print('on' not in 'dragon' and 'python')

# Exercise 16
text = 'Python'
print(float(len(text)))
print(str(len(text)))

# Exercise 17
def check_even(number):
    if number % 2 == 0:
        print(f'Number {number} is even')
    else:
        print(f'Number {number} is odd')

def check_even_auto():
    for number in range(1000):
        if number % 2 == 0:
            print(f'Number {number} is even')
        else:
            print(f'Number {number} is odd')
        time.sleep(.5)


# Exercise 18
floor = 7//3
print(floor == int(2.7))

# Exercise 19
print(type('10') == type(10))

# Exercise 20
print(int(9.8) == 10)

# Exercise 21
def cal_salary():
    hour = float(input("Enter hours: "))
    rate_per_hour = float(input("Enter rate per hour: "))
    result = hour * rate_per_hour
    result = int(result)
    print(f'Your weekly earning is {result}')

# Exercise 22
def cal_yearlive():
    have_lived = int(input('Enter number of years you have lived: '))
    result = have_lived * 365 * 24 * 60 * 60
    result = "{:,}".format(result)
    print(f"You have lived for {result} seconds. ")

# Exercise 23
def make_matrix():
    row_1 = [1, 1, 1, 1, 1]
    row_2 = [1, 1, 1, 1, 1]
    row_3 = [1, 1, 1, 1, 1]
    row_4 = [1, 1, 1, 1, 1]
    row_5 = [1, 1, 1, 1, 1]

    row_2[0] = 2
    row_3[0] = 2 + 1
    row_4[0] = 2 + 2
    row_5[0] = 2 + 3

    row_2[2] = 2
    row_3[2] = 2 + 1
    row_4[2] = 2 + 2
    row_5[2] = 2 + 3

    row_2[3] = row_2[0] * row_2[2]
    row_3[3] = row_3[0] * row_3[2]
    row_4[3] = row_4[0] * row_4[2]
    row_5[3] = row_5[0] * row_5[2]

    row_2[4] = row_2[2] * row_2[3]
    row_3[4] = row_3[2] * row_3[3]
    row_4[4] = row_4[2] * row_4[3]
    row_5[4] = row_5[2] * row_5[3]

    print('  '.join(map(str, row_1)))
    print('  '.join(map(str, row_2)))
    print('  '.join(map(str, row_3)))
    print('  '.join(map(str, row_4)))
    print('  '.join(map(str, row_5)))


make_matrix()

print("\nDay 3 Complete!")