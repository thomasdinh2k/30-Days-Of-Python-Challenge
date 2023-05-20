import string, random


def random_user_id():
    user_id = []
    for i in range(6):
        flag = random.randrange(0, 2)
        if flag == 0:
            user_id.append(string.ascii_letters[random.randrange(0, 57)].lower())
        elif flag == 1:
            user_id.append(str(random.randrange(0, 11)))
    print(f"Your new user_id is: {''.join(user_id)}")
    print(len(user_id))


def user_id_gen_by_user():
    char_num = int(input("How many character?\n"))
    id_amount = int(input("How many id?\n"))
    for i in range(id_amount):
        user_id = []  # Blank dictionary
        for k in range(char_num):
            flag = random.randrange(0, 2)
            if flag == 0:
                user_id.append(string.ascii_letters[random.randrange(0, 53)].lower())
            elif flag == 1:
                user_id.append(str(random.randrange(0, 11)))
        print(f"{''.join(user_id)}")


def rgb_color_gen():
    r = random.randrange(0, 256)
    g = random.randrange(0, 256)
    b = random.randrange(0, 256)
    print(f"rgb({r},{g},{b})")


def list_of_hexa_colors():
    hexa_color = []
    hexa_color.append("#")
    for i in range(6):
        flag = random.randrange(0, 2)
        if flag == 0:
            hexa_color.append(string.ascii_letters[random.randrange(0, 7)])  # Letter
        else:
            hexa_color.append(str(random.randrange(11)))
    print(''.join(hexa_color))


def list_of_rgb_colors(num_colors):
    colors = []
    for _ in range(num_colors):
        red = random.randint(0, 255)
        green = random.randint(0, 255)
        blue = random.randint(0, 255)
        colors.append((red, green, blue))
    return colors


def generate_color(type, amount):
    if str(type).lower() == 'hexa':
        color_list = []
        for k in range(amount):
            hexa_color = []
            hexa_color.append("#")
            for i in range(6):
                flag = random.randrange(0, 2)
                if flag == 0:
                    hexa_color.append(string.ascii_letters[random.randrange(0, 7)])  # Letter
                else:
                    hexa_color.append(str(random.randrange(11)))
            color_list.append(''.join(hexa_color))
        return color_list
    elif str(type).lower() == 'rgb':
        colors = []
        for _ in range(amount):
            red = random.randint(0, 255)
            green = random.randint(0, 255)
            blue = random.randint(0, 255)
            colors.append(f"rgb({red}, {green}, {blue})")
        return colors


def shuffle_list(list=[]):
    new_list = []
    while len(list) > 0:
        k = random.randrange(len(list) + 1)  # Take a random position in the list to append to new list
        new_list.append(str(list[k - 1]))
        list.pop(k - 1)
    print(new_list)


def random_7():
    number_array = []
    for i in range(8):
        print(f"i = {i}")
        number = random.randint(0, 9)
        print(number)
        if number not in number_array:
            number_array.append(number)
        else:
            i -= 1
    print(number_array)


random_7()
