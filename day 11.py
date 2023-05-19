def add_two_number(a, b):
    return a + b

def area_of_circle(r, pi=3.14):
    return pi*r*r

def check_all_num(*number):
    total = 0
    number_list = []
    for item in number:
        if type(item) is int:
            total += item
            number_list.append(item)
        else:
            print(f"{item} is not a number, skipping!")
    print(number_list)
    print(total)

def convert_C_to_F(c):
    f = (c * 9/5) + 32
    return f

def check_season(month):
    if 1 <= month <= 4:
        return "Spring"
    elif 5 <= month <=7:
        return "Summer"
    elif 8 <= month <= 10:
        return "Fall"
    elif 11 < month < 13:
        return "Winter"
    else:
        return "N/a"

def calculate_slope(equation):
    print(equation)
    term = equation.split()
    slope = term[2][:-1]
    return slope

import math

def solv_quadratic_eqn(a, b, c):
    def find_delta(a, b, c):
        delta = b**2-4*a*c
        return delta
    if a == 0:
        return "Can't solve quadratic equation as a = 0"
    else:
        if find_delta(a, b, c) < 0:
            return f"There are no result since delta = {find_delta(a, b, c)}"
        elif find_delta(a,b,c) == 0:
            result = -(b/2*a)
            return f"Two duplicate value x1 = x2 = {int(result)}"
        elif find_delta(a,b,c) > 0:
            x1 = ((-b) + math.sqrt(find_delta(a, b, c)))/(2*a)
            x2 = ((-b) - math.sqrt(find_delta(a, b, c)))/(2*a)
            return x1, x2

print(solv_quadratic_eqn(4, -2, -6))
print(solv_quadratic_eqn(2, -7, 3))
print(solv_quadratic_eqn(3, 2, 5))
print(solv_quadratic_eqn(1, -4, 4))