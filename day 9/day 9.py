def driving_age():
    age = int(input("How old are you?\n"))
    if age >= 18:
        print("You are old enough to drive")
    elif 5 < age < 18:
        print(f"You need {18 - age} more year(s) to learn to drive")
    else:
        print("What\'s a car?")


def compare_age():
    my_age = 23
    your_age = int(input("How old are you\n"))
    comparison = my_age - your_age
    if comparison > 0:
        print(f"I\'m {comparison} years older than you kid")
    elif comparison == 0:
        print("We are the same age, pal")
    else:
        print(f"You\'re {comparison * -1} years older than me")


def student_grade(mark):
    if 80 < mark < 100:
        print("A")
    elif 70 < mark < 89:
        print("B")
    elif 60 < mark < 69:
        print("C")
    elif 50 < mark < 59:
        print("D")
    else:
        print("F")


from datetime import datetime


def current_season():
    current_month = int(datetime.now().month)
    if 1 < current_month < 4:
        print(f"Current month is {current_month} which is SPRING")
    elif 5 <= current_month < 7:
        print(f"Current month is {current_month} which is SUMMER")
    elif 7 <= current_month < 9:
        print(f"Current month is {current_month} which is FALL")
    elif 9 <= current_month <= 12:
        print(f"Current month is {current_month} which is WINTER")
    else:
        print(f"Invalid Month {current_month} {type(current_month)}")


fruits = ['banana', 'orange', 'mango', 'lemon']


def fruit():
    fruit_input = input("Think of a fruit: \n")
    if fruit_input in fruits:
        print("That fruit already exist in the list")
        print(fruits)
    else:
        fruits.append(fruit_input.lower())
        print(f"{fruit_input} added")
        print(fruits)

person={
'first_name': 'Asabeneh',
'last_name': 'Yetayeh',
'age': 250,
'country': 'Finland',
'is_marred': False,
'skills': ['JavaScript', 'React', 'Node', 'MongoDB', 'Python'],
'address': {
    'street': 'Space street',
    'zipcode': '02210'}
}

def check_person():
    print(person['skills'][len(person['skills'])//2]) if 'skills' in person else None
    print("This guy can do Python!" if 'Python' in person['skills'] else print("He can\'t do Python"))

    if 'React' in person['skills'] and 'Node' in person['skills'] and 'MongoDB' in person['skills']:
        print("This guy can do Full-stack!!! Hire him now")
    elif 'JavaScript' in person['skills'] and 'React' in person['skills']:
        print("Front-end developer")
    elif 'Node' in person['skills'] and 'Python' in person['skills'] and 'MongoDB' in person['skills']:
        print("Back-end developer")
    else:
        print("Unknown title")

    print(f"{person['first_name'] +' ' +person['last_name']} lives in {person['country']}. He is married!") if person['is_marred'] is True else print(f"{person['first_name'] +' ' +person['last_name']} lives in {person['country']}")


print("Day 9 completed!")