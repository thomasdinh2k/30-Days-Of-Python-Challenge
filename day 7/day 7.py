# sets
it_companies = {'Facebook', 'Google', 'Microsoft', 'Apple', 'IBM', 'Oracle', 'Amazon'}
A = {19, 22, 24, 20, 25, 26}
B = {19, 22, 20, 25, 26, 24, 28, 27}
age = [22, 19, 24, 25, 26, 24, 25, 24]


def level_1():
    print(len(it_companies))
    it_companies.add("Twitter")
    print(it_companies)
    it_companies.update(["Nvidia", "FPT"])
    print(it_companies)
    it_companies.pop()
    print(it_companies)


def level_2():
    C = A.union(B)  # Join
    print(C)
    D = A.intersection(B)  # Intersection
    print(D)


def level_3():
    age_set = set(age)
    print(len(age))
    print(len(age_set))
    print('''The main different between Set and List are: 
    1. List is ordered and mutable, can be indexed 
    2. Set does not allow duplicated value 
    3. Membership and uniqueness: Lists are useful when you want to preserve the order of elements and allow duplicates, 
    while sets are primarily used when you want to ensure uniqueness and perform fast membership tests. 
    Sets provide efficient lookup operations, which makes them suitable for tasks like removing 
    duplicates from a list or checking if an element exists in a collection.
    ''')

    print('''Useful use cases of sets are:
            1. Remove Duplicates
            2. Membership testing: sets suitable for tasks like filtering out unwanted elements or
               quickly finding common elements between multiple sets.
               
            It's important to note that sets are not designed for operations that require element ordering. 
            If the order of elements is important, you should use lists instead. 
            Sets excel in scenarios where uniqueness, membership tests, and set operations are the primary requirements.
            ''')


print("Day 7 Completed!")
