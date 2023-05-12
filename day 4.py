# Exercise 3
company = "Coding For All"


# Exercise 20
def make_abbreviation(string):
    string_abb = string.split()
    for i in range(len(string_abb)):
        string_abb[i] = string_abb[i][0]
    print("".join(string_abb))


# Exercise 25
def Slice_out_phrase(sentence, slice_part):
    left_index = sentence.index(slice_part)
    right_index = len(slice_part) + left_index
    print(sentence[:left_index] + sentence[right_index:])


# Slice_out_phrase('You cannot end a sentence with because because because is a conjunction',
#                        'because because because')
#
# Slice_out_phrase('You are a gay gay gay gay person',
#                  'gay gay gay gay')
# Exercise 30
def Remove_spaces(sentence):
    print(sentence.strip())


Remove_spaces('   Coding For All      ')


# Exercise 31
def join_list(List):
    print(' # '.join(List))


join_list(['Django', 'Flask', 'Bottle', 'Pyramid', 'Falcon'])


# Exercise 34
def Exercise_34():
    print("Name\tAge\tCountry\tCity")
    print("Thomas\t23\tVietnam\tHanoi")


# Exercise 35
def Exercise_35(radius):
    area = 3.14 * radius ** 2
    print('The area of circle with radius {} is {} meters square'.format(str(radius), int(area)))


print("Day 4 completed!")
