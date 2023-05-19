from InteractiveData.CountriesData import country_fact


def add_two_number(a, b):
    return a + b


def area_of_circle(r, pi=3.14):
    return pi * r * r


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
    f = (c * 9 / 5) + 32
    return f


def check_season(month):
    if 1 <= month <= 4:
        return "Spring"
    elif 5 <= month <= 7:
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
        delta = b ** 2 - 4 * a * c
        return delta

    if a == 0:
        return "Can't solve quadratic equation as a = 0"
    else:
        if find_delta(a, b, c) < 0:
            return f"There are no result since delta = {find_delta(a, b, c)}"
        elif find_delta(a, b, c) == 0:
            result = -(b / 2 * a)
            return f"Two duplicate value x1 = x2 = {int(result)}"
        elif find_delta(a, b, c) > 0:
            x1 = ((-b) + math.sqrt(find_delta(a, b, c))) / (2 * a)
            x2 = ((-b) - math.sqrt(find_delta(a, b, c))) / (2 * a)
            return x1, x2


def print_list(list):
    [print(item) for item in list]


def reverse_list(list):
    for i in range(len(list), 0, -1):
        print(list[i - 1])


def capitalize_list_items(list):
    capitalized = []
    for item in list:
        capitalized.append(str(item).capitalize())
    return capitalized


food_staff = ['Potato', 'Tomato', 'Mango', 'Milk']
numbers = [2, 3, 7, 9]


def add_item(list=food_staff, *items):
    for i in items:
        list.append(i)
    return list


def remove_item(list=food_staff, *items):
    for item in items:
        list.remove(item)
    return list


def sum_all_number(number):
    result = 0
    while number > 0:
        result += number
        number -= 1
    return result


def sum_all_by_type(number, type='even'):
    result = 0
    if str(type).lower() == 'odd':
        while number > 0:
            if number % 2 != 0:
                result += number
                number -= 1
            else:
                number -= 1
        return result
    else:
        while number > 0:
            if number % 2 == 0:
                result += number
                number -= 1
            else:
                number -= 1
        return result


def even_and_odd(number):
    odd_count = 0
    even_count = 0
    initial_number = number
    while number >= 0:
        if number % 2 == 0:
            odd_count += 1
            number -= 1
        elif number % 2 != 0:
            even_count += 1
            number -= 1
    print(f"[{initial_number}] The number of odds are {odd_count}\n      The number of evens are {even_count}.")


def factorial(number):
    i = 1
    list_num = []
    while i <= number:
        list_num.append(i)
        i += 1
    result_string = ''
    result_int = 0
    for item in list_num:
        result_string += str(item) + '⋅'
    result_int = list_num[0] * list_num[1]
    for k in range(2, len(list_num)):
        result_int = result_int * list_num[k]
    result_string = result_string[:-1]
    print(f"{number}! = {result_string} = {result_int}")


def is_empty(*args):
    for item in args:
        if item == '':
            print("Empty")
        else:
            print(item)


import math


def total_calc(list=[]):
    total = 0
    for item in list:
        total += item
    print(f"Total = {total}")
    print(f"Mean = {total / len(list)}")
    median_position = len(list) // 2
    print(f"Median = {list[median_position]}")
    # Calculate Mode by finding the most duplicated number in the list
    unique_number = set()
    number_freq = {}
    for number in list:
        unique_number.add(number)
        if number in unique_number:
            if number not in number_freq:
                number_freq[number] = 0
            else:
                pass
            number_freq[number] += 1
        else:
            number_freq[number] = 1
    mode = max(number_freq.items(), key=lambda x: x[1])
    print(f"Mode = {mode[0]}")
    print(f"Range ({min(list)}:{max((list))}) = {(max(list) - min(list))}")
    variance = sum((x - (total / len(list))) ** 2 for x in list) / len(list)
    print(f"Variance = {variance}")
    standard_deviation = math.sqrt(sum((x - (total / len(list))) ** 2 for x in numbers) / len(numbers))
    print(f"Standard_deviation = {standard_deviation}")


def is_prime(number_list=[]):
    prime = []
    non_prime = []
    for number in number_list:
        flag = 0  # If it is a prime number, change the flag to 1
        if number == 0 or number == 1:
            flag = 1

        for i in range(2, number // 2 + 1):
            if number % i == 0:  # Check if its divisible
                flag = 1
                break

        if flag == 0:
            prime.append(number)
            print(f"{number} is a prime")
        else:
            non_prime.append(number)
            print(f"{number} is not a prime")

    print(f"Prime numbers are {''.join(str(prime))}")
    print(f"Non-prime numbers are {''.join(str(non_prime))}")


def check_unique(list=[]):
    flag = 0  # 0 means unique
    unique_set = []
    for item in list:
        count = list.count(item)
        if count == 1:
            pass
        elif count > 1:
            flag = 1
            break
    if flag != 0:
        print(f"This is not an unique list! because there are {count} number {item}")
    else:
        print(f'The list {list} is unique!')


def check_datatype(list=[]):
    data_type = type(list[0])
    for item in list[1:]:
        if type(item) != data_type:
            print("Not Same")
            return
    print("Same")


def is_valid_variable(variable):
    if not isinstance(variable, str):
        return "Can't be a variable"
    return f"{variable} can be a variable"


def country_facts():
    pop_count = {}
    language_set = set()

    for item in country_fact:
        language_set.update(item['languages'])
        country = item['name']
        population = item['population']
        if country in pop_count:
            pop_count[country] += population
        else:
            pop_count[country] = population

    lang_count = {}
    for item in language_set:
        lang_count[item] = 0
    for item in country_fact:
        for lang in item["languages"]:
            lang_count[lang] += 1

    sorted_lang_count = sorted(list(lang_count.items()), key=lambda x: x[1], reverse=True)
    top_lang = sorted_lang_count[:10]
    output_str = ""
    for i, (key, value) in enumerate(top_lang):
        output_str += f"{i + 1}. {key}: {value}\n"
    print(f"Top 10 spoken languages:\n{output_str}")

    sorted_pop_count = sorted(list(pop_count.items()), key=lambda x: x[1], reverse=True)
    top_pop = sorted_pop_count[:10]
    output_str = ""
    for i, (key, value) in enumerate(top_pop):
        output_str += f"{i + 1}. {key}: {value}\n"
    print(f"Top 10 populated countries:\n{output_str}")


print("Day 11 Completed!")
