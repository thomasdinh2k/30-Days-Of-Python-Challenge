import random


Valorant_agents = ['Astra', 'Breach', 'Brimstone', 'Chamber', 'Cypher', 'Jett', 'Kay/O', 'Killjoy', 'Neon',
                   'Omen', 'Phoenix',
                   'Raze', 'Reyna', 'Sage', 'Skye', 'Sova', 'Viper', 'Yoru']

mixed_data_types = ['Thomas', 23, 183, 'Unmarried', 'Hanoi']
it_companies = ['Facebook', 'Google', 'Microsoft', 'Apple', 'IBM', 'Oracle', 'Amazon']
test = False


# Exercise 5
def get_lst_items(lst):
    print(f"First list item is {lst[0]}")
    print(f"Item at the middle is {lst[(len(lst) // 2)]}")
    print(f"Last list item is {lst[-1]}")


if test is True:
    print(it_companies)  # Exercise 7
    print(len(it_companies))  # Exercise 8
    print(f'{it_companies[0]} {it_companies[(len(it_companies) // 2)]} {it_companies[-1]}')  # Exercise 9
    it_companies[it_companies.index('Facebook')] = 'Meta'
    print(it_companies)  # Exercise 10
    it_companies.append("FPT")
    print(it_companies)  # Exercise 11
    it_companies.insert(len(it_companies) // 2, "Nvidia")  # Exercise 12
    print(it_companies)


# Exercise 13
def change_case(lst=it_companies):
    index = random.randrange(0, len(lst))
    if lst[index].upper() is not True:
        lst[index] = lst[index].upper()
    else:
        print(f"{lst[index]} is already Uppercase)")
    print(lst[index])
    print(lst)


if test is True:
    print('#; '.join(it_companies))  # Exercise 14
    print('Nvidia' in it_companies)
    print(it_companies.count("Nvidia"))  # Exercise 15
    it_companies.sort()
    print(it_companies)  # Exercise 16
    it_companies.reverse()
    print(it_companies)  # Exercise 17


# Exercise 18 - 25
def list_actions(lst=it_companies):
    print(lst)
    print(lst[3:])
    print(lst[(len(lst)) - 3:])
    print(lst[(len(lst)) // 2:len(lst) // 2 + 1])
    lst.pop(0)
    print(lst)
    lst.pop(len(lst) // 2)
    print(lst)
    lst.pop(-1)
    print(lst)
    lst.clear()
    print(lst)
    del lst
    print(lst)


front_end = ['HTML', 'CSS', 'JS', 'React', 'Redux']
back_end = ['Node', 'Express', 'MongoDB']

if test is True:
    full_stack = front_end + back_end
    print(full_stack)
    index = full_stack.index('Redux')
    full_stack[index + 1:index + 1] = ["Python", "SQL"]  # Exercise 27
    print(full_stack)

ages = [19, 22, 19, 24, 20, 25, 26, 24, 25, 24]


def calc_age(age_lst=ages):
    age_lst.sort()
    print(age_lst)
    print(min(age_lst))
    age_lst.append(min(age_lst))
    print(max(age_lst))
    age_lst.append(max(age_lst))
    age_lst.sort()
    print(age_lst)
    median_age = age_lst[len(age_lst) // 2:len(age_lst) // 2 + 2]
    print([age / 2 for age in median_age])
    average = sum(age_lst) / len(age_lst)
    print(average)
    range_age = max(age_lst) - min(age_lst)
    print(range_age)
    min_age = min(age_lst)
    max_age = max(age_lst)
    if abs(min_age - average) > abs(max_age - average):
        print(f"(min - average) > (max- average)")
    else:
        print(f"(min - average) < (max- average)")


from InteractiveData.country import countries

if test is True:
    print(countries)
    print(countries[len(countries)//2])
    print(len(countries))
    countries_part_1 = countries[0:97]
    countries_part_2 = countries[97:]

    print(countries_part_1)
    print(countries_part_2)
    print(len(countries_part_1))
    print(len(countries_part_2))

    need_to_unpack = ['China', 'Russia', 'USA', 'Finland', 'Sweden', 'Norway', 'Denmark']
    first_country, second_country, third_country, *rest = need_to_unpack
    print(first_country)

print("Day 5 complete!")