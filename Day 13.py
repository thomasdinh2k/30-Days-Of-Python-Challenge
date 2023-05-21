numbers = [-4, -3, -2, -1, 0, 2, 4, 6]
list_of_lists = [[[1, 2, 3]], [[4, 5, 6]], [[7, 8, 9]]]


def negative_and_zero(list=numbers):
    result = [i for i in numbers if i <= 0]
    print(result)


def flattened_list(list=list_of_lists):
    print([number for row in list for sub_row in row for number in sub_row])

def make_list_of_number_tuples():
    print([tuple([number] + [number**i for i in range(6)]) for number in range(11)])


countries = [[('Finland', 'Helsinki')], [('Sweden', 'Stockholm')], [('Norway', 'Oslo')]]
def flatten_list():
    print([[item[0].upper(), item[0][:3].upper(), item[1].upper()] for row in countries for item in row])

def list_of_dictionary(countries=countries):
    dict = {}
    final_list = []
    # for row in countries:
    #     for items in row:
    #         dict["country"] = items[0].upper()
    #         dict["city"] = items[1].upper()
    #     final_list.append(dict)
    # print(final_list)

    print([{"country":items[0].upper(), 'city':items[1].upper()} for row in countries for items in row])


def list_of_string():
    names = [[('Asabeneh', 'Yetayeh')], [('David', 'Smith')], [('Donald', 'Trump')], [('Bill', 'Gates')]]
    print([' '.join(item) for row in names for item in row])


def linear_functions(equation='y = 20x + 103'):
    terms = equation.split()
    a = terms[2][:-1]
    b = terms[4]
    print(f"Slope = {a}\nY-intercept= {b}")


linear_solver = lambda equation, variable: eval(equation.replace(variable, 'x'))

slope = linear_solver('y = 20x + 103', 'slope')

print(slope)