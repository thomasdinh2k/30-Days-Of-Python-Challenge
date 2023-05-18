from InteractiveData.country import countries

def iterate(start_num, end_num, direction):
    if direction == 'forward':
        print(f"Iterating from {start_num} to {end_num}")
        print("Using For")
        for number in range(start_num, end_num + 1):
            print(number)
        print("Using While")
        count = start_num
        while count <= end_num:
            print(count)
            count += 1
    elif direction == 'backward':
        temporary_variable = start_num
        start_num = end_num
        end_num = temporary_variable
        print(f"Iteration from {start_num} to {end_num} (backward)")
        print("Using For")
        for number in range(start_num, end_num, -1):
            print(number)
        print("Using While")
        count = start_num
        while count >= end_num:
            print(count)
            count -= 1


def make_triangle(calls):
    i = 0
    while i <= calls+1:
        if i == 0:
            i += 1
        else:
            print('#' * i)
            i += 1


def make_sqr(length):
 step = 0
 if length <= 0:
     print(f"Can\'t make a shape out of given length {length}")
 else:
     for i in range(length):
         print("# " * length)


def multiplication_table(number):
    for multiplier in range(10+1):
        result = number * multiplier
        print(f"{number} x {multiplier} = {result}")


def lang_items():
    lang = ['Python', 'Numpy','Pandas','Django', 'Flask']
    [print(item) for item in lang]
    [print(item) for item in lang if item.startswith("F")]


def iterate_number(number, type):
    if type == 'even':
        [print(num) for num in range(number) if num % 2 == 0]
    else:
        [print(num) for num in range(number) if num % 2 != 0]


def sum_all(number, type=""):
    total = 0
    if type == 'All':
        for i in range(number + 1):
            total += i
        print(total)
    elif type == 'Odd':
        for i in range(number + 1):
            if i % 2 != 0:      # Odd-number
                total += i
        print(total)
    elif type == 'Even':
        for i in range(number + 1):
            if i % 2 == 0:      # Even-number
                total += i
        print(total)
    else:
        total_even = 0
        total_odd = 0
        for i in range(number + 1):
            if i % 2 != 0:      # Odd-number
                total_odd += i
            if i % 2 == 0:  # Even-number
                total_even += i
        print(f"The sum of all evens is {total_even}. And the sum of all odds is {total_odd}")


def print_country():
    [print(item) for item in countries if 'land' in item]


def reverse_order(lst):
    reversed_lst = []
    for i in range(len(lst)-1, -1, -1):
        print(lst[i])
        reversed_lst.append(lst[i])
    print(reversed_lst)

from InteractiveData.
def country_facts():
    print(country_fact)

country_facts()
